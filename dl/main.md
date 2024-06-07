---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
import torch
torch.cuda.is_available()
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B", device_map="auto")

```

```python
tokenizer.add_special_tokens({"pad_token": "[PAD]"})
```

```python
import json
from datasets import Dataset

def load_data(path):
    with open(path, "r") as f:
        data = [json.loads(line) for line in f]
    

load_data("data.jsonl")
```





















```python
import json
with open('data.jsonl') as f:
    data = [json.loads(line) for line in f]

with open("data_.jsonl", "w", encoding="utf-8") as f:
    for sample in data:
        atad = {"input": "", "output": []}
        for i in sample:
            atad["input"] = list(sample.keys())[0]
            atad["output"] = list(sample.values())[0]
        json_line = json.dumps(atad, ensure_ascii=False)
        f.write(json_line + "\n")
```

