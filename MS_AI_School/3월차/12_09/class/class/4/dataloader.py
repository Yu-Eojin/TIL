import os
import pandas as pd
import torchvision.transforms
from torchvision.io import read_image
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from torch import nn
from classification import Classifier, MSNet
from torchvision.transforms import ToTensor
from torch import optim
import torch

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file, names=['file_name', 'label'])
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label


dataset = CustomImageDataset(
    annotations_file='/home/bong08/mskim/infinyx/pythonProject/4/data/FashionMNIST/annotations.csv',
    img_dir='/home/bong08/mskim/infinyx/pythonProject/4/data/FashionMNIST/imgs',
    )

dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

model = Classifier()
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=0.003)
epochs = 20

for e in range(epochs):
    running_loss = 0
    for images, labels in dataloader:
        # 모델에서 훈련
        print(images.shape)
        result = model(images)
        # 오차 계산
        loss = criterion(result, labels)

        # 초기화
        optimizer.zero_grad()
        # 역전파
        loss.backward()
        # 스텝
        optimizer.step()

        # 오차값을 총 오차에 더함
        running_loss += loss.item()
    else:
        print(f"Training loss: {running_loss/len(dataloader)}")


model = Classifier()
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=0.003)

epochs = 30
steps = 0

train_losses, test_losses = [], []
for e in range(epochs):
    running_loss = 0
    for images, labels in dataloader:

        optimizer.zero_grad()

        log_ps = model(images)
        loss = criterion(log_ps, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    # for 문이 끝나면 실행한다.
    else:
        test_loss = 0
        accuracy = 0

        # Turn off gradients for validation, saves memory and computations
        # 자동 미분을 꺼서 pytorch가 쓸 떼 없는 짓을 안하게 한다. (어차피 test set에서 하는 작업이므로)
        with torch.no_grad():
            for images, labels in dataloader:
                log_ps = model(images)
                test_loss += criterion(log_ps, labels)

                # 로그 확률에 지수 적용
                ps = torch.exp(log_ps)
                # topk는 k번째로 큰 숫자를 찾아내는 것이다.
                # dim=1 는 dimension을 의미한다.
                top_p, top_class = ps.topk(1, dim=1)
                # labels를 top_class와 똑같은 형태로 만든다음에, 얼마나 같은게 있는지 확인한다.
                equals = top_class == labels.view(*top_class.shape)
                # equals를 float으로 바꾸고 평균 정확도를 구한다.
                accuracy += torch.mean(equals.type(torch.FloatTensor))

        train_losses.append(running_loss/len(dataloader))
        test_losses.append(test_loss/len(dataloader))

        print("Epoch: {}/{}.. ".format(e+1, epochs),
              "Training Loss: {:.3f}.. ".format(running_loss/len(dataloader)),
              "Test Loss: {:.3f}.. ".format(test_loss/len(dataloader)),
              "Test Accuracy: {:.3f}".format(accuracy/len(dataloader)))