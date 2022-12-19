from sklearn.model_selection import train_test_split
import glob
import os
import shutil


# 데이터 나누기(train 80%, validation 10%, test 10%)
'''
폴더 구조
data
    - train
        - orange
            - 01.png
        - grapefruit
        - kanpei
        - dekopon
    - val
            - orange
                - 01.png
        - grapefruit
        - kanpei
        - dekopon
    - test
            - orange
                - 01.png
        - grapefruit
        - kanpei
        - dekopon
'''

# 이미지 경로 설정
image_path = './dataset/image/'

# orange 이미지 경로에 대한 list
orange_data = glob.glob(os.path.join(image_path,'orange','*.png'))
# grapefruit 이미지 경로에 대한 list
grapefruit_data = glob.glob(os.path.join(image_path,'grapefruit','*.png'))
# kanpei 이미지 경로에 대한 list
kanpei_data = glob.glob(os.path.join(image_path,'kanpei','*.png'))
# dekopon 이미지 경로에 대한 list
dekopon_data = glob.glob(os.path.join(image_path,'dekopon','*.png'))

# train val (9:1)
orange_data_train, orange_data_val = train_test_split(
    orange_data, test_size=0.1, random_state=7777
)
grapefruit_data_train, grapefruit_data_val = train_test_split(
    grapefruit_data, test_size=0.1, random_state=7777
)
kanpei_data_train, kanpei_data_val = train_test_split(
    kanpei_data, test_size=0.1, random_state=7777
)
dekopon_data_train, dekopon_data_val = train_test_split(
    dekopon_data, test_size=0.1, random_state=7777
)

for i in orange_data_train :
    file_name = os.path.basename(i)
    os.makedirs('./data/train/orange/', exist_ok=True)
    shutil.move(i,f'./data/train/orange/orange_{file_name}' )

for i in orange_data_val:
    file_name = os.path.basename(i)
    os.makedirs('./data/val/orange/', exist_ok=True)
    shutil.move(i,f'./data/val/orange/orange_{file_name}' )

for i in grapefruit_data_train :
    file_name = os.path.basename(i)
    os.makedirs('./data/train/grapefruit/', exist_ok=True)
    shutil.move(i,f'./data/train/grapefruit/grapefruit_{file_name}' )

for i in grapefruit_data_val:
    file_name = os.path.basename(i)
    os.makedirs('./data/val/grapefruit/', exist_ok=True)
    shutil.move(i,f'./data/val/grapefruit/grapefruit_{file_name}' )

for i in kanpei_data_train :
    file_name = os.path.basename(i)
    os.makedirs('./data/train/kanpei/', exist_ok=True)
    shutil.move(i,f'./data/train/kanpei/kanpei_{file_name}' )

for i in kanpei_data_val:
    file_name = os.path.basename(i)
    os.makedirs('./data/val/kanpei/', exist_ok=True)
    shutil.move(i,f'./data/val/kanpei/kanpei_{file_name}' )

for i in dekopon_data_train :
    file_name = os.path.basename(i)
    os.makedirs('./data/train/dekopon/', exist_ok=True)
    shutil.move(i,f'./data/train/dekopon/dekopon_{file_name}' )

for i in dekopon_data_val:
    file_name = os.path.basename(i)
    os.makedirs('./data/val/dekopon/', exist_ok=True)
    shutil.move(i,f'./data/val/dekopon/dekopon_{file_name}' )
