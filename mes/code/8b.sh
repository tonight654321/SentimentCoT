#!/bin/bash

# CK
# 定义一个数组，包含所有想要迭代的 num_of_shots 的值
# 循环遍历每一个 num_of_shots 的值 (implicit)
num_of_shots_values=(1 4 8)
for num in "${num_of_shots_values[@]}"
do
    echo "Running with num_of_shots=$num"
    python run_base_Cohen_Kappa.py --model_name_or_path /home/incoming/LLM/llama3/llama3-8b-instruct --prompt_name PROMPT_standard_implicit --num_of_shots $num
    sleep 20

#    python run_base_Cohen_Kappa.py --model_name_or_path /home/incoming/LLM/llama3/llama3-8b-instruct --prompt_name PROMPT_standard_explicit --num_of_shots $num
    echo "Completed with num_of_shots=$num"
#    sleep 20
done



# ------ base ----
num_of_shots_values=(1 4 8 12 15 18)
for num in "${num_of_shots_values[@]}"
do
    echo "Running with num_of_shots=$num"
    python run_base.py --model_name_or_path /home/incoming/LLM/llama3/llama3-8b-instruct --prompt_name PROMPT_standard_implicit --num_of_shots $num
    sleep 20

#    python run_base.py --model_name_or_path /home/incoming/LLM/llama3/llama3-8b-instruct --prompt_name PROMPT_standard_explicit --num_of_shots $num
    echo "Completed with num_of_shots=$num"
#    sleep 20
done


# 定义一个数组，包含所有想要迭代的 num_of_shots 的值
num_of_shots_values=(1 4 8 12 15 18)
for version in V1 V2 V3
  do
  for num in "${num_of_shots_values[@]}"
  do
      echo "Running with num_of_shots=$num"
      python run.py --model_name_or_path /home/incoming/LLM/llama3/llama3-8b-instruct --prompt_name PROMPT_implicit_COT_$version --num_of_shots $num
      sleep 20

#      python run.py --model_name_or_path /home/incoming/LLM/llama3/llama3-8b-instruct --prompt_name PROMPT_explicit_COT_$version --num_of_shots $num
      echo "Completed with num_of_shots=$num"
#      sleep 20
  done
done