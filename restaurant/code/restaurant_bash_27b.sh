# Model path
#MODEL="google/gemma-2-27b"
MODEL="/home/incoming/LLM/gemma2/gemma2-27b"

# explicit实验
SHOTS=(1 4 8 12 15 18)
VERSION=(V1 V2 V3)
CATEGORY=(explicit)

for num_shots in "${SHOTS[@]}"
do
  for category in "${CATEGORY[@]}"
  do
    for version in "${VERSION[@]}"
    do
      python run.py   --model_name_or_path $MODEL   --prompt_name PROMPT_${category}_COT_$version  --num_of_shots $num_shots
      sleep 50
    done
  done
done

num_of_shots_values=(1 4 8 12 15 18)
for num in "${num_of_shots_values[@]}"
do
    echo "Running with num_of_shots=$num"
#    python run_base.py --model_name_or_path /home/incoming/LLM/gemma2/gemma2-2b --prompt_name PROMPT_standard_implicit --num_of_shots $num
#    sleep 20

    python run_base.py --model_name_or_path /home/incoming/LLM/gemma2/gemma2-2b --prompt_name PROMPT_standard_explicit --num_of_shots $num
    echo "Completed with num_of_shots=$num"
    sleep 20
done


# implicit实验
SHOTS=(15 18)
VERSION=(V2)
CATEGORY=(implicit)

for num_shots in "${SHOTS[@]}"
do
  for category in "${CATEGORY[@]}"
  do
    for version in "${VERSION[@]}"
    do
      python run.py   --model_name_or_path $MODEL   --prompt_name PROMPT_${category}_COT_$version  --num_of_shots $num_shots
      sleep 50
    done
  done
done

# 一致性测试
#SHOTS=(1 4 8 12 15)
#CATEGORY=(implicit explicit)
#for num_shots in "${SHOTS[@]}"
#do
#  for category in "${CATEGORY[@]}"
#  do
#    echo "Running with ${num_shots} shots ${category}"
#    python run_base_Cohen_Kappa.py --model_name_or_path $MODEL --prompt_name PROMPT_standard_${category} --num_of_shots $num_shots
#    sleep 20
#done
#done


# 实验三
# input顺序打乱
#SHOTS=(1 4 8 12 15 18)
# SHOTS=(18)
# CATEGORY=(explicit implicit)
# for num_shots in "${SHOTS[@]}"
# do
#     for cat in "${CATEGORY[@]}"
#     do
#         echo "Running with ${num_shots} shots (${cat})"
#         python run_base.py --model_name_or_path $MODEL --prompt_name PROMPT_standard_${cat} --num_of_shots $num_shots --shuffle_input True
#         sleep 20
#     done
# done


# aspect情感极性反转
# SHOTS=(1 4 8 12 15 18)
# VERSIONS=(V1 V2 V3)
# CATEGORIES=(explicit implicit)
#ASPECTS_REVERSE="True"
# for num_shots in "${SHOTS[@]}"
# do
#     for category in "${CATEGORIES[@]}"
#     do
#         for version in "${VERSIONS[@]}"
#         do
#             echo "Running with ${num_shots} shots, ${category}, Version ${version}"
#             python run.py --model_name_or_path $MODEL --prompt_name PROMPT_${category}_COT_${version} --num_of_shots $num_shots --aspects_reverse True
#             sleep 20
#         done
#     done
# done