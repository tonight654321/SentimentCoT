import os
import json
from sklearn.metrics import cohen_kappa_score
import numpy as np
from collections import Counter

base_path = r"C:\Users\29911\Desktop\result\Res_result\1-shot"
top_folders = ["consistency", "实验三", "实验一"]
sub_folders = [
    r"Base\explicit",
    r"Base\implicit",
    r"COT_V1\explicit",
    r"COT_V1\implicit",
    r"COT_V2\explicit",
    r"COT_V2\implicit",
    r"COT_V3\explicit",
    r"COT_V3\implicit"
]

def extract_sentiments(file_path):
    predictions = []
    truths = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if 'generated_text' in data:
                if 'final_polarity' in data and 'final_polarity_truth' in data:
                    predictions.extend(data['final_polarity'])
                    truths.extend([data['final_polarity_truth'][1]])  
                else:
                    predictions.append('null')
                    truths.append('null')
    return predictions, truths

def standardize_model_name(model_name):
    model_name_mappings = {
        "Meta-Llama-3-8B-Instruct": "llama3-8b-instruct",
        "gemma-2-2b": "gemma2-2b",
        "gemma-2-9b": "gemma2-9b",
        "gemma-2-27b": "gemma2-27b"
    }
    return model_name_mappings.get(model_name, model_name)


def extract_files(base_path, top_folder, sub_folders):

    folder_path = os.path.join(base_path, top_folder)

    for sub_folder in sub_folders:
        full_path = os.path.join(folder_path, sub_folder)
        for file in os.listdir(full_path):
            if file.endswith('.jsonl'):
                file_path = os.path.join(full_path, file)
                predictions, truths = extract_sentiments(file_path)

                model_name = file.split('_')[-3]
                model_name = standardize_model_name(model_name)
                label = f"{top_folder}_{sub_folder.replace(os.sep, '_')}_{model_name}"

                results[label] = {
                    "predictions": predictions,
                    "truths": truths
                }

def calculate_kappa_between_predictions_and_truths(results):
    
    for label in results:
        if "consistency" in label:
            predictions = results[label]["predictions"]
            truths = results[label]["truths"]

            adjusted_predictions = []
            adjusted_truths = []
            for pred, truth in zip(predictions, truths):
                if pred == 'null' and truth == 'null':
                    adjusted_predictions.append('null_pred') 
                    adjusted_truths.append('null_truth')      
                else:
                    adjusted_predictions.append(pred)
                    adjusted_truths.append(truth)

            kappa_value = cohen_kappa_score(adjusted_predictions, adjusted_truths)

            ck_results_truths[label] = kappa_value

    return ck_results_truths

def calculate_kappa_between_experiments(results):

    for label in results:
        if "实验一" in label:
            corresponding_label = label.replace("实验一", "实验三")
            if corresponding_label in results:

                predictions_exp1 = results[label]["predictions"]
                predictions_exp3 = results[corresponding_label]["predictions"]

                kappa_value = cohen_kappa_score(predictions_exp1, predictions_exp3)

                ck_results_experiments[label] = kappa_value
    
    return ck_results_experiments

def normalize_ck_values(ck_results_truths):
    
    normalized_weights = {}
    temp_dict = {}

    for label, ck_value in ck_results_truths.items():
        parts = label.split('_')

        if parts[1] in ['Base']:
            prefix = '_'.join(parts[:3])
        else:
            prefix = '_'.join(parts[:4])
        
        if prefix not in temp_dict:
            temp_dict[prefix] = []
        
        temp_dict[prefix].append((label, ck_value))
    
    for prefix, ck_items in temp_dict.items():
        total_ck_value = sum(ck_value for _, ck_value in ck_items)
        
        if total_ck_value > 0:
            normalized_ck_values = [(label, ck_value / total_ck_value) for label, ck_value in ck_items]
        else:
            normalized_ck_values = [(label, 0) for label, _ in ck_items]

        for label, ck in normalized_ck_values:
            normalized_weights[label] = ck

    for label, weight in normalized_weights.items():
        print(f"{label} 的归一化权重 = {weight:.4f}")

    return normalized_weights

def match_weights(results, normalized_weights):

    for label, data in results.items():
        if label.startswith("实验一") or label.startswith("consistency"):
            label_suffix = label.split('_', 1)[-1] 
            
            for norm_label, weight in normalized_weights.items():
                if norm_label.endswith(label_suffix):
                    matched_results[label] = {
                        "predictions": data['predictions'],
                        "truths": data['truths'],
                        "weight": weight
                    }
                    break  
    return matched_results

def weighted_vote(predictions_list, weights):

    combined_vote_counter = []

    num_samples = len(predictions_list[0])  
    for i in range(num_samples):
        vote_counter = Counter()
        for j, predictions in enumerate(predictions_list):
            vote_counter[predictions[i]] += weights[j]
        combined_vote_counter.append(vote_counter)

    final_labels = [vote_counter.most_common(1)[0][0] for vote_counter in combined_vote_counter]
    
    return final_labels

def group_and_vote(matched_results):
    
    grouped_results = {}


    for label, data in matched_results.items():

        if not label.startswith("实验一"):
            continue

        parts = label.split('_')

        if parts[1] in ['Base']:
            prefix = '_'.join(parts[:3])
        else:
            prefix = '_'.join(parts[:4])
        
        if prefix not in grouped_results:
            grouped_results[prefix] = []
        
        grouped_results[prefix].append((label, data))

    for prefix, models in grouped_results.items():
        predictions_list = [data['predictions'] for _, data in models]
        weights = [data['weight'] for _, data in models]

        final_labels = weighted_vote(predictions_list, weights)

        for label, data in models:
            data['truths'] = final_labels 

    return grouped_results

def calculate_accuracy(grouped_results):
    accuracy_results = {}

    for prefix, models in grouped_results.items():
        for label, data in models:
            predictions = data['predictions']
            truths = data['truths']

            correct_predictions = sum(1 for pred, truth in zip(predictions, truths) if pred == truth)
            total_samples = len(truths)
            accuracy = correct_predictions / total_samples if total_samples > 0 else 0

            accuracy_results[label] = accuracy

    return accuracy_results

def extract_aspect_accuracy(base_path, top_folder, sub_folders):
    aspect_accuracy_results = {}

    folder_path = os.path.join(base_path, top_folder)

    for sub_folder in sub_folders:
        full_path = os.path.join(folder_path, sub_folder)
        for file in os.listdir(full_path):
            if file.endswith('.jsonl'):
                file_path = os.path.join(full_path, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        data = json.loads(line)
                        if "Aspect Average Accuracy" in data:
                            aspect_accuracy = data["Aspect Average Accuracy"]
                            model_name = file.split('_')[-3]
                            model_name = standardize_model_name(model_name)
                            label = f"{top_folder}_{sub_folder.replace(os.sep, '_')}_{model_name}"
                            aspect_accuracy_results[label] = aspect_accuracy
                            print(f"Extracted {label}: {aspect_accuracy}")
                            break 

    return aspect_accuracy_results


results = {}
matched_results = {}
ck_results_experiments = {}
ck_results_truths = {}

extract_files(base_path, "consistency", sub_folders)
extract_files(base_path, "实验一", sub_folders)
extract_files(base_path, "实验三", sub_folders)
aspect_accuracy_results = extract_aspect_accuracy(base_path, "实验一", sub_folders)
calculate_kappa_between_predictions_and_truths(results)
normalized_weights = normalize_ck_values(ck_results_truths)
matched_results = match_weights(results, normalized_weights)
grouped_results = group_and_vote(matched_results)
accuracy_results = calculate_accuracy(grouped_results)
calculate_kappa_between_experiments(results)

output_file = os.path.join(base_path, "result_output.txt")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("Results:\n")
    f.write(json.dumps(results, ensure_ascii=False, indent=4))
    f.write("\n\n模型一致性_Cohen's Kappa (Truths):\n")
    f.write(json.dumps(ck_results_truths, ensure_ascii=False, indent=4))
    f.write("\n\n实验一—_Accuracy Results:\n")
    f.write(json.dumps(accuracy_results, ensure_ascii=False, indent=4))
    f.write("\n\n实验一—_Aspect Average Accuracy:\n")
    f.write(json.dumps(aspect_accuracy_results, ensure_ascii=False, indent=4))
    f.write("\n\n实验三—_Cohen's Kappa (Experiments):\n")
    f.write(json.dumps(ck_results_experiments, ensure_ascii=False, indent=4))

print(f"所有结果已保存到 {output_file}")