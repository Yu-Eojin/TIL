import pandas as pd

a= pd.read_csv('4/data/FashionMNIST/annotations.csv', names=['file_name','label'], skiprows=[0])
print(a)

print([i for i in a['file_name'] if 'png' not in i=='file_name'])