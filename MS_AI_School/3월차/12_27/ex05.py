# 클래스로 파이토치 모델 구현 : 로지스틱회귀
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# train data -> Tensor
x_data = [[1,2], [2,3], [3,1], [4,3], [5,3], [6,2]]
y_data = [[0], [0], [0], [1], [1], [1]]

# Tensor
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

class BinaryClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 1) # input dim = 2, output dim = 1
        self.sigmoid = nn.Sigmoid()   # 출력은 시그모이드 함수를 거침

    def forward(self, x):
        return self.sigmoid(self.linear(x))

# 모델 호출
model = BinaryClassifier()

# 옵티마이저 설정
optimizer = optim.SGD(model.parameters(), lr=0.1)

# train loop
epoch_num = 1000
for epoch in range(epoch_num + 1):
    
    output = model(x_train)

    #loss
    loss = F.binary_cross_entropy(output, y_train)

    # loss update
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # print
    if epoch % 10 == 0:
        prediction = output >= torch.FloatTensor([0.5]) # 예측값이 0.5 넘으면 True로 간주
        correct_prediction = prediction.float() == y_train # 실제값과 일치하는 경우만 True
        acc = correct_prediction.sum().item() / len(correct_prediction) # 정확도 계산
        print('Epoch {:4d}/{} loss: {:.6f} acc: {:.2f}'.format(
            epoch, epoch_num, loss.item(), acc*100
        ))

print(model(x_train))
