from transformers import pipeline
import pandas as pd

# pipline() >> 함수를 호출하면서 관심 작업 이름을 전달해 파이프라인 객체를 생성
# 다양한 파이프라인 정보 >> https://huggingface.co/docs/transformers/main/en/pipeline_tutorial#pipeline-usage
classifier = pipeline('text-classification')

text = """Dear Amazon, last week I ordered an Optimus Prime action figure \
from your online store in Germany. Unfortunately, when I opened the package, \
I discovered to my horror that I had been sent an action figure of Megatron \
instead! As a lifelong enemy of the Decepticons, I hope you can understand my \
dilemma. To resolve the issue, I demand an exchange of Megatron for the \
Optimus Prime figure I ordered. Enclosed are copies of my records concerning \
this purchase. I expect to hear from you soon. Sincerely, Bumblebee."""

# output = classifier(text)
# print(output)

# # 객체인식
# ner_tagger = pipeline('ner', aggregation_strategy='simple')
# output = ner_tagger(text)
# temp = pd.DataFrame(output)
# print(temp)

# reder = pipeline('question-answering')
# question = 'What does the customer want?'
# output = reder(question=question, context=text)
# temp1 = pd.DataFrame([output])
# print(temp1)

# summarizer = pipeline('summarization')
# output = summarizer(text, max_length=60, clean_up_tokenization_spaces=True)
# print(output[0]['summary_text'])

# pipe = pipeline('translation', model='Helsinki-NLP/opus-mt-ja-en')
# print(pipe('愚か者'))

from transformers import set_seed
set_seed(888)

generator = pipeline('text-generation')
response = 'Dear Bumblebee, I am sorry to hear that your order was mixed up.'
prompt = text + '\n\nCustomer service respose : \n' + response
output = generator(prompt, max_length=200)
print(output[0]['generated_text'])