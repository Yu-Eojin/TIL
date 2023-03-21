import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 랜덤 시드 설정
torch.manual_seed(1)

# 실습을 위한 기본셋팅 훈련데이터 x_train, y_train을 선언
x_train = torch.FloatTensor(([1], [2], [3]))
y_train = torch.FloatTensor(([2], [4], [6]))

# 훈련데이터 shape 출력
# print(x_train, x_train.shape) # shape or size
# print(y_train, y_train.size()) # shape or size

# 가중치와 편향 초기화 직선 -> w, b
w = torch.zeros(1, requires_grad=True) # requires_grad > 학습을 통해 값이 업데이트 되게 설정하는 옵션
# print(w)
b = torch.zeros(1, requires_grad=True)
# print(b)

# 가설 세우기
# 직선의 방정식
hypothesis = x_train * w + b

# loss func 선언하기 
# 평균 제곱 오차 선언
loss = torch.mean((hypothesis - y_train) ** 2)

# 경사하강법 구현
optimizer = optim.SGD([w, b], lr=0.01)

# 기울기 0으로 초기화
optimizer.zero_grad()
loss.backward()

# 학습 진행
epoch_num = 2000
# epoch : 전체 훈련 데이터가 학습에 한번 사용된 주기

# train loop
for epoch in range(epoch_num+1):
    
    # 1. 가설
    hypothesis = x_train * w + b

    # 2. loss 계산
    loss = torch.mean((hypothesis - y_train) ** 2)

    # 3. loss를 이용한 가설(H(x)) 개선
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 100번 마다 print
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} W: {:.3f} b: {:.3f} loss:{:.6f}'.format(
            epoch, epoch_num, w.item(), b.item(), loss.item()
        ))
