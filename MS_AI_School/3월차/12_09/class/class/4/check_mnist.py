import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2

labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

mnist_data = pd.read_csv('./4/data/FashionMNIST/annotations.csv', names=['file_name', 'label'], skiprows=[0])

print(len(mnist_data))
print(len(os.listdir('./4/data/FashionMNIST/imgs')))

img_dir = './4/data/FashionMNIST/imgs'
for i in range(len(mnist_data)):
    file_name, label = mnist_data.iloc[i]
    img = cv2.imread(os.path.join(img_dir, file_name))
    
    plt.subplots(1,5,i+1)
    plt.imshow(img, 'gray')
    plt.title(labels_map[label])
plt.show()