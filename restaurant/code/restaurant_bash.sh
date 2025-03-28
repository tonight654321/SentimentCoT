# 遗漏实验

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 15

sleep 15

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 18

sleep 15

# explicit实验

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18


## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18


## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18


## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18


# 一致性测试
## implicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit --num_of_shots 1
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit --num_of_shots 1
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit --num_of_shots 1  
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_implicit --num_of_shots 1


## explicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit --num_of_shots 1
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit --num_of_shots 1
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit --num_of_shots 1
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_explicit --num_of_shots 1


## implicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit --num_of_shots 4
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit --num_of_shots 4
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit --num_of_shots 4  
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_implicit --num_of_shots 4


## explicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit --num_of_shots 4
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit --num_of_shots 4
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit --num_of_shots 4
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_explicit --num_of_shots 4

## implicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit --num_of_shots 8
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit --num_of_shots 8
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit --num_of_shots 8  
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_implicit --num_of_shots 8


## explicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit --num_of_shots 8
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit --num_of_shots 8
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit --num_of_shots 8
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_explicit --num_of_shots 8

## implicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit --num_of_shots 12
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit --num_of_shots 12
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit --num_of_shots 12  
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_implicit --num_of_shots 12


## explicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit --num_of_shots 12
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit --num_of_shots 12
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit --num_of_shots 12
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_explicit --num_of_shots 12

## implicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit --num_of_shots 15
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit --num_of_shots 15
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit --num_of_shots 15  
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_implicit --num_of_shots 15


## explicit
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit --num_of_shots 15
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit --num_of_shots 15
python run_base_Cohen_Kappa.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit --num_of_shots 15
python run_base_Cohen_Kappa.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_standard_explicit --num_of_shots 15


# 实验三

# input顺序打乱

## gemma2-2b

python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit  --num_of_shots 1 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit  --num_of_shots 1 --shuffle_input True

## gemma2-9b

python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit  --num_of_shots 1 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit  --num_of_shots 1 --shuffle_input True

## gemma2-27b

python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit  --num_of_shots 1 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit  --num_of_shots 1 --shuffle_input True

## llama3-8b

python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_explicit --num_of_shots 1 --shuffle_input True
python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_implicit --num_of_shots 1 --shuffle_input True

# aspect情感极性反转

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 1 --aspects_reverse True 
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 1 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 1 --aspects_reverse True

## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 1 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 1 --aspects_reverse True

## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 1 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 1 --aspects_reverse True

## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 1 --aspects_reverse True

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 1 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 1 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 1 --aspects_reverse True


# input顺序打乱

## gemma2-2b

python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit  --num_of_shots 4 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit  --num_of_shots 4 --shuffle_input True

## gemma2-9b

python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit  --num_of_shots 4 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit  --num_of_shots 4 --shuffle_input True

## gemma2-27b

python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit  --num_of_shots 4 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit  --num_of_shots 4 --shuffle_input True

## llama3-8b

python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_explicit --num_of_shots 4 --shuffle_input True
python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_implicit --num_of_shots 4 --shuffle_input True

# aspect情感极性反转

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 4 --aspects_reverse True 
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 4 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 4 --aspects_reverse True

## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 4 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 4 --aspects_reverse True

## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 4 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 4 --aspects_reverse True

## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 4 --aspects_reverse True

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 4 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 4 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 4 --aspects_reverse True

# input顺序打乱

## gemma2-2b

python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit  --num_of_shots 8 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit  --num_of_shots 8 --shuffle_input True

## gemma2-9b

python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit  --num_of_shots 8 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit  --num_of_shots 8 --shuffle_input True

## gemma2-27b

python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit  --num_of_shots 8 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit  --num_of_shots 8 --shuffle_input True

## llama3-8b

python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_explicit --num_of_shots 8 --shuffle_input True
python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_implicit --num_of_shots 8 --shuffle_input True

# aspect情感极性反转

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 8 --aspects_reverse True 
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 8 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 8 --aspects_reverse True

## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 8 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 8 --aspects_reverse True

## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 8 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 8 --aspects_reverse True

## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 8 --aspects_reverse True

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 8 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 8 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 8 --aspects_reverse True

# input顺序打乱

## gemma2-2b

python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit  --num_of_shots 12 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit  --num_of_shots 12 --shuffle_input True

## gemma2-9b

python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit  --num_of_shots 12 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit  --num_of_shots 12 --shuffle_input True

## gemma2-27b

python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit  --num_of_shots 12 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit  --num_of_shots 12 --shuffle_input True

## llama3-8b

python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_explicit --num_of_shots 12 --shuffle_input True
python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_implicit --num_of_shots 12 --shuffle_input True

# aspect情感极性反转

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 12 --aspects_reverse True 
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 12 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 12 --aspects_reverse True

## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 12 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 12 --aspects_reverse True

## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 12 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 12 --aspects_reverse True

## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 12 --aspects_reverse True

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 12 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 12 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 12 --aspects_reverse True

# input顺序打乱

## gemma2-2b

python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit  --num_of_shots 15 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit  --num_of_shots 15 --shuffle_input True

## gemma2-9b

python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit  --num_of_shots 15 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit  --num_of_shots 15 --shuffle_input True

## gemma2-27b

python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit  --num_of_shots 15 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit  --num_of_shots 15 --shuffle_input True

## llama3-8b

python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_explicit --num_of_shots 15 --shuffle_input True
python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_implicit --num_of_shots 15 --shuffle_input True

# aspect情感极性反转

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 15 --aspects_reverse True 
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 15 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 15 --aspects_reverse True

## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 15 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 15 --aspects_reverse True

## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 15 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 15 --aspects_reverse True

## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 15 --aspects_reverse True

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 15 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 15 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 15 --aspects_reverse True


# input顺序打乱

## gemma2-2b

python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_explicit  --num_of_shots 18 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_standard_implicit  --num_of_shots 18 --shuffle_input True

## gemma2-9b

python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_explicit  --num_of_shots 18 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_standard_implicit  --num_of_shots 18 --shuffle_input True

## gemma2-27b

python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_explicit  --num_of_shots 18 --shuffle_input True
python run_base.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_standard_implicit  --num_of_shots 18 --shuffle_input True

## llama3-8b

python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_explicit --num_of_shots 18 --shuffle_input True
python run_base.py  --model_name_or_path /root/commonData/Meta-Llama-3-8B-Instruct   --prompt_name PROMPT_standard_implicit --num_of_shots 18 --shuffle_input True

# aspect情感极性反转

## gemma2-2b

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 18 --aspects_reverse True 
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 18 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-2b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18 --aspects_reverse True

## gemma2-9b

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 18 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-9b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18 --aspects_reverse True

## gemma2-27b

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 18 --aspects_reverse True

python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py   --model_name_or_path google/gemma-2-27b   --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18 --aspects_reverse True

## llama3-8b

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_implicit_COT_V3  --num_of_shots 18 --aspects_reverse True

python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V1  --num_of_shots 18 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V2  --num_of_shots 18 --aspects_reverse True
python run.py  --model_name_or_path   /root/commonData/Meta-Llama-3-8B-Instruct  --prompt_name PROMPT_explicit_COT_V3  --num_of_shots 18 --aspects_reverse True