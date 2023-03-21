import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.data import TensorDataset, DataLoader

x_train = torch.FloatTensor([[73, 80, 75], 
                            [93, 88, 90], 
                            [83, 99, 80], 
                            [96, 70, 20], 
                            [73, 40, 75]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# TensorDataset 입력으로 사용하고 dataset 지정
dataset = TensorDataset(x_train, y_train)

# dataloader
dataloader = DataLoader(dataset, batch_size= 2, shuffle=True)

# 모델 설계
model = nn.Linear(3,1)
optimizer = optim.SGD(model.parameters(), lr=1e-5)

# train loop
epoch_num = 300
for epoch in range(epoch_num+1):
    for batch_idx, sample in enumerate(dataloader):
        x_train, y_train = sample

        # 모델 선언
        prediction = model(x_train)

        # loss
        loss = F.mse_loss(prediction, y_train)

        # loss update
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print('Epoch {:4d}/{} batch {}/{} loss:{:.6f}'.format(
                epoch, epoch_num, batch_idx+1, len(dataloader), loss.item()
            ))

test_val = torch.FloatTensor([[73, 80, 75]])
pred_y = model(test_val)
print(f'훈련 후 입력이 {test_val} 예측값: {pred_y}')