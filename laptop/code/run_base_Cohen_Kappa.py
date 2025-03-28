# 在\laptop\code目录下运行 python run_base.py --r_file ../data/test.xml --model_name_or_path "../../model/gemma-2b-it" --prompt_name PROMPT_standard_explicit
import random
import re
import pandas as pd
import torch
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

def generate(num_shots, prompt, text_list, final_polarity_truth, model_name_or_path, max_new_tokens):
    # 加载模型和分词器
    model, tokenizer = load_models(model_name_or_path)

    # 存储所有预测结果
    results = []

    # 迭代处理每个输入句子
    for text, pol in zip(text_list, final_polarity_truth):
        print(text)
        # 将prompt和text拼接成一个输入，并进行分词处理
        input_text = f"{prompt}\nReview:{text.strip()}"
        inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

        # 使用模型进行预测，设置生成的最大长度
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, output_hidden_states=True,
                                     return_dict_in_generate=True, pad_token_id=tokenizer.eos_token_id)

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

            # 逐个标记地解码和打印生成的标记，并添加索引
            decoded_tokens = [tokenizer.decode([token_id], skip_special_tokens=False) for token_id in
                              input_and_out_sequence]
            for index, (token_id, decoded_token) in enumerate(zip(input_and_out_sequence, decoded_tokens)):
                print(f"Index: {index}, Token ID: {token_id}, Decoded Token: {decoded_token}")

            # print("Shape of input_and_output_hidden_states:", input_and_output_hidden_states.shape)
            input_indices, output_indices = extract_indices_and_tokens(input_and_out_sequence, decoded_tokens)

            # 生成热力图
            generate_heatmap(input_and_output_hidden_states, decoded_tokens, input_indices, output_indices,
                             output_file_figure, pol[0])

    # 返回所有生成的文字结果和相关数据
    return results

def extract_matching_results(generated_text, text):
    pattern = re.compile(r'Review:\s*(.*?)\s*Sentiment:\s*(\w+)', re.DOTALL)
    matches = pattern.findall(generated_text)

    for match in matches:
        review_text = match[0].strip()
        if review_text.startswith(text.strip()):  # 太hard了，容易识别不了
            sentiment = match[1].strip()
            result = {
                "Review": review_text,
                "Sentiment": sentiment
            }
            return result
    return None

def read_exemplar(prompt, file_path, n=10):
    tree = ET.parse(file_path)
    root = tree.getroot()

    sentences = []
    final_polarity_truth = []
    exemplar = prompt[-n:]

    for idx, sentence in enumerate(exemplar):
        sentence_text = sentence.split('\n')[1].split('Review: ')[-1]
        polarity = sentence.strip().split('Sentiment: ')[-1]
        sentences.append(sentence_text)
        final_polarity_truth.append([str(idx), polarity])

    return sentences, final_polarity_truth


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


def extract_indices_and_tokens(input_and_out_sequence, decoded_tokens):
    input_indices = []
    output_indices = []
    recording_output = False
    start_found = False
    review_count = 0
    target_review_count = 19

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
            if decoded_token == "\n" or token_id == 1:
                break
            input_indices.append(index)
    for index, (token_id, decoded_token) in enumerate(zip(input_and_out_sequence, decoded_tokens)):
        if index == input_indices[-1]+3:
            recording_output = True
        elif recording_output:
            if decoded_token == "\n" or token_id == 1:
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
    heatmap_file = os.path.join(output_file_figure, f"heatmap_{prompt_name}_{timestamp}_{label}.pdf")
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


def write_and_cal():
    final_polarity_predict = []

    with open(output_file_json, "w", encoding="utf-8") as file:
        for j, result in enumerate(results):
            match_result = extract_matching_results(result, text_list[j].strip())
            if match_result:
                final_polarity = [match_result['Sentiment']]
                index = text_list[j].split(':')[0]
                final_polarity_predict.append([index] + final_polarity)

                output_data = {
                    "review": text_list[j],
                    "generated_text": result,
                    "final_polarity": final_polarity,
                    "final_polarity_truth": final_polarity_truth[j]
                }
            else:
                output_data = {
                    "generated_text": result,
                }
            file.write(json.dumps(output_data, ensure_ascii=False) + "\n")
    final_average_acc, final_match_details = calculate_final_polarity_acc(final_polarity_predict, final_polarity_truth)

    # 也写到function里，不放主函数里
    with open(output_file_json, "a", encoding="utf-8") as file:
        for index, match in enumerate(final_match_details):
            file.write(json.dumps({
                "Final Polarity Index": final_polarity_predict[index][0],
                "Match": match,
                "Prediction": final_polarity_predict[index][1],
                "Truth": final_polarity_truth[index][1]
            }, ensure_ascii=False) + "\n")

        file.write(json.dumps({"Final Polarity Average Accuracy": final_average_acc}, ensure_ascii=False) + "\n")

    print(f"Results saved to {output_file_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('--r_file', type=str, default='../data/Laptops_Test_Train_Gold_Implicit_Labeled.xml',
                        help='Path to the input XML file')
    # parser.add_argument('--model_name_or_path', type=str, default='../../model/gemma-2b-it', help='Model name or path')
    parser.add_argument('--model_name_or_path', type=str, default='D:\phd6\parttime\COT\cot\gemma-2b',
                        help='Model name or path')
    parser.add_argument('--max_new_tokens', type=int, default=100, help='Maximum number of new tokens to generate')
    parser.add_argument('--prompt_name', type=str, default='PROMPT_standard_implicit', help='Prompt name')
    parser.add_argument('--num_of_shots', type=int, default=4, help='the number of demonstrations')

    args = parser.parse_args()

    r_file = args.r_file
    model_name = args.model_name_or_path.split("/")[-1]
    max_new_tokens = args.max_new_tokens
    prompt_name = args.prompt_name
    tested_num_each = 18 - args.num_of_shots

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # 定义结果保存路径
    result_dir = os.path.join(base_dir, 'result')
    figure_dir = os.path.join(result_dir, 'figure')

    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    if not os.path.exists(figure_dir):
        os.makedirs(figure_dir)


    output_file_json = os.path.join(result_dir,
                                    f"results_CK_{prompt_name}_{args.num_of_shots}-shot_{model_name}_{timestamp}.jsonl")
    output_file_figure = figure_dir

    # 读取XML文件中的句子和标签
    prompt = get_prompt_from_modules(prompt_name)
    text_list, final_polarity_truth = read_exemplar(prompt, r_file, n=tested_num_each)

    extracted_prompts = "\n".join([re.sub(r'\n\s*Sentiment:', '\nSentiment:', text.strip()) for text in prompt[:args.num_of_shots]])
    results = generate(args.num_of_shots, extracted_prompts, text_list, final_polarity_truth, args.model_name_or_path, max_new_tokens)

    write_and_cal()





