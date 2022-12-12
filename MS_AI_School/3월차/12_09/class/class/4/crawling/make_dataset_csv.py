import pandas as pd
import os
from collections import defaultdict

data_dir = '/home/bong08/mskim/infinyx/pythonProject/4/crawling/data'

label_list = []
for label in os.listdir(data_dir):
    print(label)
    label_list.append(label)

df_dict = defaultdict(list)

for idx, label in enumerate(label_list):
    label_index = idx
    label_name = label
    for image in os.listdir(os.path.join(data_dir, label_name)):
        # img_path = os.path.join(data_dir, label_name, image)
        df_dict['file_name'].append(os.path.join(label_name, image))
        df_dict['label'] = label_index

df = pd.DataFrame(df_dict)
df.to_csv('data/annotations.csv')
