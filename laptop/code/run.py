import re
import pandas as pd
import torch
import random
import datetime
import os
from load_LLMs import load_models
import importlib
import argparse
import json
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from matplotlib.colors import LinearSegmentedColormap


def generate(num_shots, prompt, text_list, final_polarity_truth, model_name_or_path, max_new_tokens, prompt_name, aspects_reverse):
    # 加载模型和分词器
    model, tokenizer = load_models(model_name_or_path)

    # 存储所有预测结果
    results = []

    if aspects_reverse:
        prompt = reverse_aspects(prompt, prompt_name)

    # 迭代处理每个输入句子
    for text, pol in zip(text_list, final_polarity_truth):
        print(text)
        # 将prompt和text拼接成一个输入，并进行分词处理
        input_text = f"{prompt}\nReview:{text.strip()}"
        inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

        # 使用模型进行预测，设置生成的最大长度
        with torch.no_grad():
            # https://huggingface.co/docs/transformers/main_classes/text_generation
            outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, output_hidden_states=True,
                                     return_dict_in_generate=True, pad_token_id=tokenizer.eos_token_id)
            # outputs = model.generate(**inputs, max_new_tokens=70, output_hidden_states=True,
            #                          return_dict_in_generate=True, pad_token_id=tokenizer.eos_token_id,
            #                          temperature =0.5, do_sample=True, top_k=10, top_p=0.9)

        hidden_states = outputs.hidden_states
        generated_ids = outputs.sequences
        # 解码生成的token为文字
        generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        # 将结果添加到列表中
        results.append(generated_text)

        # 提取输入和输出的索引     # 生成热力图， 随机画4*3张图
        if random.random() < 0.0:
            # 提取最后一层的输入隐藏状态
            last_input_hidden_states = hidden_states[0][-1]
            # 获取最后一层输出的隐藏状态，并拼接
            last_output_hidden_states = torch.cat([item[-1] for i, item in enumerate(hidden_states) if i != 0], dim=1)

            # 拼接输入和输出的隐藏状态
            input_and_output_hidden_states = torch.cat([last_input_hidden_states, last_output_hidden_states], dim=1)

            # 获取输入和输出的序列
            input_and_out_sequence = generated_ids.tolist()[0][1:]

            # 逐个标记地解码和打印生成的标记，并添加索引--测试使用
            decoded_tokens = [tokenizer.decode([token_id], skip_special_tokens=False) for token_id in
                              input_and_out_sequence]
            for index, (token_id, decoded_token) in enumerate(zip(input_and_out_sequence, decoded_tokens)):
                print(f"Index: {index}, Token ID: {token_id}, Decoded Token: {decoded_token}")

            print("Shape of input_and_output_hidden_states:", input_and_output_hidden_states.shape)
            input_indices, output_indices = extract_indices_and_tokens(input_and_out_sequence, decoded_tokens,
                                                                       num_shots=num_shots,model_name=model_name)
            generate_heatmap(input_and_output_hidden_states, decoded_tokens, input_indices, output_indices,
                             output_file_figure, pol[0])

    # 返回所有生成的文字结果和相关数据
    return results


def extract_matching_results(generated_text, text):
    pattern = re.compile(r'Review:\s*(.*?)\s*COT:\s*(.*?)\s*Sentiment:\s*(\w+)', re.DOTALL)
    matches = pattern.findall(generated_text)

    for match in matches:
        review_text = match[0].strip()
        if review_text.startswith(text.strip()):  # 太hard了，容易识别不了
            cot_text = match[1].strip()
            sentiment = match[2].strip()
            result = {
                "Review": review_text,
                "COT": cot_text,
                "Sentiment": sentiment
            }
            return result
    return None


def extract_polarities(cot_text):
    # 提取COT:中的情感极性
    aspect_polarity_pattern = re.compile(r'(positive|negative|neutral)')
    aspect_polarities = aspect_polarity_pattern.findall(cot_text)

    return aspect_polarities


# 读取XML文件并提取句子和标签
def read_xml(prompt_name, file_path, n=10,shuffle_input=False):
    tree = ET.parse(file_path)
    root = tree.getroot()

    sentences = []
    aspect_polarity_truth = []
    final_polarity_truth = []

    one_aspect_sentence, one_aspect_polarity_truth, one_final_polarity_truth = [], [], []
    two_aspect_sentence, two_aspect_polarity_truth, two_final_polarity_truth = [], [], []
    three_aspect_sentence, three_aspect_polarity_truth, three_final_polarity_truth = [], [], []
    four_aspect_sentence, four_aspect_polarity_truth, four_final_polarity_truth = [], [], []

    implicit = "False"
    if 'implicit' in prompt_name:
        implicit = "True"

    for idx, sentence in enumerate(root.findall('sentence')):
        implicit_sentiment = list(set([aspect.get('implicit_sentiment') for aspect in sentence.findall('aspectTerms/aspectTerm')]))
        # 只处理纯隐式或纯显式的句子
        if len(implicit_sentiment) == 1 and implicit_sentiment[0] == implicit:
            polarities = [aspect.get('polarity') for aspect in sentence.findall('aspectTerms/aspectTerm')]
            sentence_text = f"{idx}: {sentence.find('text').text}".split(':')[1]
            # 只测试10个文本
            if len(polarities) == 1 and len(one_aspect_sentence) < n:
                while len(polarities) < 4:
                    polarities.append('null')
                if shuffle_input:
                    sentence_text = shuffle_sentence(sentence_text)
                one_aspect_sentence.append(sentence_text)
                one_aspect_polarity_truth.append([str(idx)] + polarities)
                one_final_polarity_truth.append([str(idx), 'positive'])
            elif len(polarities) == 2 and len(two_aspect_sentence) < n:
                while len(polarities) < 4:
                    polarities.append('null')
                if shuffle_input:
                    sentence_text = shuffle_sentence(sentence_text)
                two_aspect_sentence.append(sentence_text)
                two_aspect_polarity_truth.append([str(idx)] + polarities)
                two_final_polarity_truth.append([str(idx), 'positive'])
            elif len(polarities) == 3 and len(three_aspect_sentence) < n:
                while len(polarities) < 4:
                    polarities.append('null')
                if shuffle_input:
                    sentence_text = shuffle_sentence(sentence_text)
                three_aspect_sentence.append(sentence_text)
                three_aspect_polarity_truth.append([str(idx)] + polarities)
                three_final_polarity_truth.append([str(idx), 'positive'])
            elif len(polarities) == 4 and len(four_aspect_sentence) < n:
                if shuffle_input:
                    sentence_text = shuffle_sentence(sentence_text)
                four_aspect_sentence.append(sentence_text)
                four_aspect_polarity_truth.append([str(idx)] + polarities)
                four_final_polarity_truth.append([str(idx), 'positive'])

        sentences = one_aspect_sentence + two_aspect_sentence + three_aspect_sentence + four_aspect_sentence
        aspect_polarity_truth = one_aspect_polarity_truth + two_aspect_polarity_truth + three_aspect_polarity_truth + four_aspect_polarity_truth
        final_polarity_truth = one_final_polarity_truth + two_final_polarity_truth + three_final_polarity_truth + four_final_polarity_truth

    return sentences, aspect_polarity_truth, final_polarity_truth

def shuffle_sentence(sentence_text):
    words = sentence_text.split()
    shuffled_words = []
    for i in range(0, len(words), 2):
        if i + 1 < len(words):
            shuffled_words.extend([words[i+1], words[i]])
        else:
            shuffled_words.append(words[i])
    shuffled_sentence = ' '.join(shuffled_words)
    return shuffled_sentence


def calculate_aspect_polarity_acc(aspect_polarity_predict, aspect_polarity_truth):
    def single_sample_acc(pred, truth):
        pred_aspects = [p for p in pred[1:] if p != 'null']
        truth_aspects = [t for t in truth[1:] if t != 'null']

        max_len = max(len(pred_aspects), len(truth_aspects))
        match_count = 0
        match_details = []

        for i in range(4):
            if pred[i + 1] == 'null' or truth[i + 1] == 'null':
                match_details.append(0)
            else:
                if pred[i + 1] == truth[i + 1]:
                    match_details.append(1)
                    match_count += 1
                else:
                    match_details.append(0)

        acc = match_count / max_len if max_len > 0 else 0
        return acc, match_details

    total_acc = 0
    all_match_details = []

    for pred, truth in zip(aspect_polarity_predict, aspect_polarity_truth):
        acc, match_details = single_sample_acc(pred, truth)
        total_acc += acc
        all_match_details.append((pred[0], match_details, acc))

    average_acc = total_acc / len(aspect_polarity_predict) if len(aspect_polarity_predict) > 0 else 0

    return average_acc, all_match_details


def calculate_final_polarity_acc(final_polarity_predict, final_polarity_truth):
    match_count = 0
    total_count = len(final_polarity_predict)
    match_details = []

    for pred, truth in zip(final_polarity_predict, final_polarity_truth):
        if pred[1] == truth[1]:
            match_count += 1
            match_details.append(1)
        else:
            match_details.append(0)

    acc = match_count / total_count if total_count > 0 else 0
    return acc, match_details


def extract_indices_and_tokens(input_and_out_sequence, decoded_tokens, num_shots, model_name):
    input_indices = []
    output_indices = []
    recording_output = False
    start_found = False
    review_count = 0
    target_review_count = num_shots + 1

    if "gemma" in model_name.lower():
        model_type = "gemma"
    elif "llama" in model_name.lower():
        model_type = "llama"
    else:
        raise ValueError(f"Unsupported model type for model_name: {model_name}")

    # 首先找到start_index
    for index, (token_id, decoded_token) in enumerate(zip(input_and_out_sequence, decoded_tokens)):
        if decoded_token.strip() == "Review":
            review_count += 1
            if review_count == target_review_count:
                start_index = index + 1
                break

    for index, (token_id, decoded_token) in enumerate(zip(input_and_out_sequence, decoded_tokens)):
        if index == start_index:
            start_found = True
        elif start_found:
            # 根据模型类型选择不同的结束条件
            if model_type == "gemma":
                if decoded_token == "\n":
                    break
            elif model_type == "llama":
                if decoded_token == "C":  
                    break
            input_indices.append(index)
    
    for index, (token_id, decoded_token) in enumerate(zip(input_and_out_sequence, decoded_tokens)):
        if index == input_indices[-1] + 3:
            recording_output = True
        elif recording_output:
            # 根据模型类型选择不同的结束条件
            if model_type == "gemma":
                if decoded_token == "\n":
                    break
            elif model_type == "llama":
                if decoded_token == "Sent": 
                    break
            output_indices.append(index)

    return input_indices, output_indices



def generate_heatmap(input_and_output_hidden_states, decoded_tokens, input_indices, output_indices, output_file_figure,
                     label):
    # 提取输入序列和输出序列的隐藏状态
    input_hidden_states = input_and_output_hidden_states[0, input_indices, :]
    output_hidden_states = input_and_output_hidden_states[0, output_indices, :]

    # 提取对应的token字符
    input_tokens = [decoded_tokens[i] for i in input_indices]
    output_tokens = [decoded_tokens[i] for i in output_indices]

    # 计算余弦相似度
    similarity_matrix = cosine_similarity(input_hidden_states.cpu().numpy(), output_hidden_states.cpu().numpy())
    similarity_matrix = np.round(similarity_matrix, 2)

    # 自定义颜色映射
    colors = ["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43",
              "#d73027", "#a50026"]
    n_bins = 100  # 将插值离散化为多个颜色区间
    cmap_name = 'custom_cmap'
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    # 生成热力图
    plt.figure(figsize=(15, 8))
    ax = sns.heatmap(similarity_matrix, annot=True, cmap=custom_cmap, xticklabels=output_tokens,
                     yticklabels=input_tokens, fmt=".2f")
    plt.title('Cosine Similarity Heatmap')
    plt.xlabel('Output Texts', labelpad=1)
    plt.ylabel('Input Texts', labelpad=15)
    plt.xticks(rotation=45, ha='right')

    label = label
    heatmap_file = os.path.join(output_file_figure, f"heatmap_{prompt_name}_{args.num_of_shots}-shot_{model_name}_{timestamp}_{label}.jpg")
    plt.savefig(heatmap_file)


def get_prompt_from_modules(prompt_name):
    # 尝试从 prompts_implicit 模块导入
    try:
        prompts_module_implicit = importlib.import_module('prompts_implicit')
        if hasattr(prompts_module_implicit, prompt_name):
            return getattr(prompts_module_implicit, prompt_name)
    except ImportError:
        pass

    # 尝试从 prompts_explicit 模块导入
    try:
        prompts_module_explicit = importlib.import_module('prompts_explicit')
        if hasattr(prompts_module_explicit, prompt_name):
            return getattr(prompts_module_explicit, prompt_name)
    except ImportError:
        pass

    # 如果两个模块中都没有找到，则抛出异常
    raise ValueError(f"Prompt name {prompt_name} not found in either prompts_implicit.py or prompts_explicit.py")

def reverse_aspects(prompt_text, prompt_name):
    def reverse_label(label):
        if label == "positive":
            return "negative"
        elif label == "negative":
            return "positive"
        elif label == "neutral":
            return random.choice(["positive", "negative"])

    def reverse_cot_v1(cot_text):
        labels = re.findall(r'\b(positive|negative|neutral)\b', cot_text)
        reversed_labels = [reverse_label(label) for label in labels[:-1]]
        reversed_labels.append(labels[-1])
        for original, reversed_label in zip(labels, reversed_labels):
            cot_text = cot_text.replace(original, reversed_label, 1)
        return cot_text

    def reverse_cot_v2(cot_text):
        return re.sub(r'\((\s*(neutral|positive|negative)\s*(?:,\s*(neutral|positive|negative)\s*)*)\)', 
                    lambda match: f"({', '.join(reverse_label(label.strip()) for label in match.group(1).split(','))})", 
                    cot_text)
    
    def reverse_cot_v3(cot_text):
        aspects = cot_text.split("->")
        reversed_aspects = [reverse_label(aspect.strip()) for aspect in aspects[:-1]]
        reversed_aspects.append(aspects[-1].strip()) 
        return " -> ".join(reversed_aspects)
    
    pattern = re.compile(r'Review:\s*(.*?)\s*COT:\s*(.*?)\s*Sentiment:\s*(\w+)', re.DOTALL)
    matches = pattern.findall(prompt_text)

    reversed_prompts = []

    for match in matches:
        review = match[0].strip()
        cot = match[1].strip()
        sentiment = match[2].strip()

        if "COT_V1" in prompt_name:
            reversed_cot = reverse_cot_v1(cot)
        elif "COT_V2" in prompt_name:
            reversed_cot = reverse_cot_v2(cot)
        elif "COT_V3" in prompt_name:
            reversed_cot = reverse_cot_v3(cot)
        else:
            raise ValueError(f"Unsupported prompt version in {prompt_name}")
        
        reversed_prompt = f"Review: {review}\nCOT: {reversed_cot}\nSentiment: {sentiment}"
        reversed_prompts.append(reversed_prompt)

    return "\n".join(reversed_prompts)

def write_and_cal():
    aspect_polarity_predict = []
    final_polarity_predict = []

    # 保存结果到json文件，写成函数。
    with open(output_file_json, "w", encoding="utf-8") as file:
        for j, result in enumerate(results):
            match_result = extract_matching_results(result, text_list[j].strip())
            if match_result:
                aspect_polarity = extract_polarities(match_result['COT'])
                final_polarity = [match_result['Sentiment']]

                index = text_list[j].split(':')[0]

                aspect_polarity = aspect_polarity[:-1]

                while len(aspect_polarity) < 4:
                    aspect_polarity.append('null')
                aspect_polarity_predict.append([index] + aspect_polarity)
                final_polarity_predict.append([index] + final_polarity)

                output_data = {
                    "review": text_list[j],
                    "generated_text": result,
                    "aspects_polarity": aspect_polarity,
                    "final_polarity": final_polarity,
                    "aspect_polarity_truth": aspect_polarity_truth[j],
                    "final_polarity_truth": final_polarity_truth[j]
                }
            else:
                output_data = {
                    "generated_text": result,
                }
            file.write(json.dumps(output_data, ensure_ascii=False) + "\n")

    aspect_average_acc, all_match_details = calculate_aspect_polarity_acc(aspect_polarity_predict,
                                                                          aspect_polarity_truth)
    final_average_acc, final_match_details = calculate_final_polarity_acc(final_polarity_predict, final_polarity_truth)

    # 也写到function里，不放主函数里
    with open(output_file_json, "a", encoding="utf-8") as file:
        for sample in all_match_details:
            file.write(json.dumps({
                "Index": sample[0],
                "Match Details": sample[1],
                "Sample Accuracy": sample[2]
            }, ensure_ascii=False) + "\n")

        file.write(json.dumps({"Aspect Average Accuracy": aspect_average_acc}, ensure_ascii=False) + "\n")

        for index, match in enumerate(final_match_details):
            file.write(json.dumps({
                "Final Polarity Index": final_polarity_predict[index][0],
                "Match": match,
                "Prediction": final_polarity_predict[index][1],
                "Truth": final_polarity_truth[index][1]
            }, ensure_ascii=False) + "\n")

        file.write(json.dumps({"Final Polarity Average Accuracy": final_average_acc}, ensure_ascii=False) + "\n")

    print(f"Results saved to {output_file_json}")


# 使用示例
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('--r_file', type=str, default='../data/Laptops_Test_Train_Gold_Implicit_Labeled.xml', help='Path to the input XML file')
    parser.add_argument('--model_name_or_path', type=str, default='../../model/gemma-2b-it', help='Model name or path')
    # parser.add_argument('--model_name_or_path', type=str, default='D:\phd6\parttime\COT\cot\gemma-2b', help='Model name or path')
    parser.add_argument('--max_new_tokens', type=int, default=120, help='Maximum number of new tokens to generate')
    parser.add_argument('--prompt_name', type=str, default='PROMPT_implicit_COT_V1', help='Prompt name')
    parser.add_argument('--num_of_shots', type=int, default=4, help='the number of demonstrations')
    parser.add_argument('--aspects_reverse', type=bool, default=False,help='If set, reverse the aspects in COT')
    parser.add_argument('--shuffle_input', type=bool, default=False, help='Whether to shuffle the input text')

    args = parser.parse_args()

    r_file = args.r_file
    model_name = args.model_name_or_path.split("/")[-1]
    max_new_tokens = args.max_new_tokens
    prompt_name = args.prompt_name
    tested_num_each = 15

    # 获取当前脚本所在目录的路径，并切换到上一级目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 获取当前时间戳
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # 定义结果保存路径
    result_dir = os.path.join(base_dir, 'result')
    figure_dir = os.path.join(result_dir, 'figure')

    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    if not os.path.exists(figure_dir):
        os.makedirs(figure_dir)

    output_file_json = os.path.join(result_dir, f"results_{prompt_name}_{args.num_of_shots}-shot_{model_name}_{timestamp}.jsonl")
    output_file_figure = figure_dir

    # 读取XML文件中的句子和标签
    text_list, aspect_polarity_truth, final_polarity_truth = read_xml(prompt_name, r_file, n=tested_num_each,shuffle_input=args.shuffle_input)

    # 动态获取提示符变量
    prompt = get_prompt_from_modules(prompt_name)

    extracted_prompts = "\n".join(
        [re.sub(r'\n\s*(Review|COT|Sentiment):', r'\n\1:', text.strip()) for text in prompt[:args.num_of_shots]]
    )

    results = generate(args.num_of_shots, extracted_prompts, text_list, final_polarity_truth, args.model_name_or_path, max_new_tokens, prompt_name=args.prompt_name, aspects_reverse=args.aspects_reverse)

    write_and_cal()



