# utils/llm_pipeline.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

MODEL_ID = "google/flan-t5-large"

tok = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype=torch.float16
)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tok,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.4
)
