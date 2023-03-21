# 다중 선형 회귀 클래스 선언
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

x_train = torch.FloatTensor([[73, 80, 75], 
                            [93, 88, 90], 
                            [83, 99, 80], 
                            [96, 70, 20], 
                            [73, 40, 75]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# 클래스 생성
class MultiLinearRegresstionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1) # input 3, output 1
    
    def forward(self, x):
        return self.linear.forward(x)

# model 정의
model = MultiLinearRegresstionModel()

# optimizer
optimizer = optim.SGD(model.parameters(), lr=1e-5)

# train
epoch_num = 2000
for epoch in range(epoch_num+1):

    #model
    prediction = model(x_train)
    
    #loss
    loss = F.mse_loss(prediction, y_train)

    # w update
    optimizer.zero_grad() # 기울기를 0으로 초기화
    loss.backward()       # loss 함수를 미분하여 기울기계산  
    optimizer.step()      # w, b 를 업데이트

    if epoch % 100 == 0:
        print('Epoch {:4d}/{}  loss:{:.6f}'.format(
            epoch, epoch_num, loss.item()
        ))

new_var = torch.FloatTensor([[73, 82, 72]])
pred_y = model(new_var)
print(f'훈련 후 입력이 {new_var} 예측값: {pred_y}')