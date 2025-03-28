import torch


def load_gemma(model_name_or_path):
    from transformers.models.gemma import GemmaForCausalLM
    from transformers.models.gemma.tokenization_gemma import GemmaTokenizer
    global_devices = [i for i in range(torch.cuda.device_count())] if torch.cuda.device_count() >= 1 else ["cpu"]
    max_memory = {k: '32GB' for k in global_devices}
    tokenizer = GemmaTokenizer.from_pretrained(model_name_or_path, legacy=False)
    model = GemmaForCausalLM.from_pretrained(model_name_or_path,
                                             low_cpu_mem_usage=True, device_map='auto',
                                             torch_dtype=torch.float32, max_memory=max_memory
                                             )
    return model, tokenizer

def load_gemma2(model_name_or_path):
    from transformers.models.gemma2 import Gemma2ForCausalLM
    from transformers.models.gemma.tokenization_gemma import GemmaTokenizer
    global_devices = [i for i in range(torch.cuda.device_count())] if torch.cuda.device_count() >= 1 else ["cpu"]

    max_memory = {k: '32GB' for k in global_devices}
    tokenizer = GemmaTokenizer.from_pretrained(model_name_or_path, legacy=False)
    model = Gemma2ForCausalLM.from_pretrained(model_name_or_path, cache_dir='../../',
                                             low_cpu_mem_usage=True, device_map='auto', # 多卡需要
                                             torch_dtype=torch.float32, max_memory=max_memory
                                             )
    return model, tokenizer


def load_llama(model_name_or_path):
    from transformers import LlamaForCausalLM
    from transformers.models.llama.tokenization_llama import LlamaTokenizer
    global_devices = [i for i in range(torch.cuda.device_count())] if torch.cuda.device_count() >= 1 else ["cpu"]
    max_memory = {k: '32GB' for k in global_devices}
    from transformers import AutoTokenizer, AutoModelForCausalLM

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, legacy=False)
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path, cache_dir='../../',
                                             low_cpu_mem_usage=True, device_map='auto',
                                             torch_dtype=torch.float32, max_memory=max_memory
                                             )
    return model, tokenizer


def load_models(model_name_or_path):
    if 'gemma2' in model_name_or_path:
        return load_gemma2(model_name_or_path)
    elif 'gemma' in model_name_or_path:
        return load_gemma(model_name_or_path)
    elif 'llama' in model_name_or_path.lower():
        return load_llama(model_name_or_path)
    else:
        raise ValueError('Model not found')

