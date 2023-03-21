import random
import logging
import numpy as np
import pandas as pd
import datasets
from datasets import load_dataset, load_metric, ClassLabel, Sequence
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

model_checkpoint = 'klue/roberta-base'
batch_size = 128
task = 'nli'

dataset = load_dataset('klue', task)
# print(dataset['train'][0])

metric = load_metric('glue', 'qnli')
fake_preds = np.random.randint(0, 2, size=(64,))
fake_labels = np.random.randint(0, 2, size=(64,))
# print(fake_preds, fake_labels)

test = metric.compute(predictions=fake_preds, references=fake_labels)
print(test)

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)
token_test = tokenizer('안녕하세요. 저는 물범입니다.', '찬하가 저를 물범이라고 불러요. 저는 사람인데')
print(token_test)
