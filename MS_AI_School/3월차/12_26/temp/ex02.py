import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 다중 선형 회귀 실습
# 다수 x로부터 y를 예측하는 다중 선형회귀
x1_train = torch.FloatTensor([[73], [93], [83], [96], [73]])
x2_train = torch.FloatTensor([[80], [88], [91], [98], [66]])
x3_train = torch.FloatTensor([[75], [93], [90], [100], [70]]) 
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# 가중치 w와 편향 b를 선언 -> w는 3개 b는 1개
w1 = torch.zeros(1, requires_grad=True)
w2 = torch.zeros(1, requires_grad=True)
w3 = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# optimizer
optimizer = optim.SGD([w1,w2,w3,b], lr=1e-7)

epoch_num = 10000
for epoch in range(epoch_num+1):

    # 가설
    hypothesis = x1_train*w1 + x2_train*w2 + x3_train*w3 + b
    # loss
    loss = torch.mean((hypothesis - y_train) ** 2)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 출력
    if epoch %100 ==0:
        print('Epoch {:4d}/{} w1: {:.3f} w2: {:.3f} w3: {:.3f} b: {:.3f} loss: {:.6f}'.format(
            epoch, epoch_num, w1.item(), w2.item(), w3.item(), b.item(), loss.item()
        ))