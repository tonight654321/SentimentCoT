# 🧠 Reassessing the Role of Chain-of-Thought in Sentiment Analysis

## ✅ Run the Main Script
python run.py \
    --r_file ./data/Laptop.xml \
    --model_name_or_path ../../model/gemma-2b-it \
    --max_new_tokens 120 \
    --prompt_name PROMPT_implicit_COT_V1 \
    --num_of_shots 4 \
    --aspects_reverse False \
    --shuffle_input False

## 📌 Argument Descriptions

| Argument | Description |
|----------|-------------|
| `--r_file` | Path to the input XML dataset |
| `--model_name_or_path` | Local path or Huggingface name of the model |
| `--prompt_name` | Prompt variable name (must be defined in `prompts_implicit.py` or `prompts_explicit.py`) |
| `--num_of_shots` | Number of few-shot examples to include |
| `--aspects_reverse` | Whether to reverse aspect polarities in the prompt (for counterfactual experiments) |
| `--shuffle_input` | Whether to shuffle input sentence word order (for word order sensitivity tests) |


## 📈 Output Format

Each result will be saved in `.jsonl` format, structured like this:

```json
{
  "review": "This laptop looks nice but the screen is terrible.",
  "generated_text": "Review: ... COT: ... Sentiment: negative",
  "aspects_polarity": ["positive", "negative", "null", "null"],
  "final_polarity": ["negative"],
  "aspect_polarity_truth": ["positive", "negative", "null", "null"],
  "final_polarity_truth": ["negative"]
}
```












