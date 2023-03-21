# b값 변화에 따른 경사도 변화
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(t):
    return 1/(1+np.exp(-t))

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(0.5 + x)
y2 = sigmoid(x + 1)
y3 = sigmoid(x +1.5)

plt.plot(x, y1, 'r', linestyle='--') # w값이 0.5
plt.plot(x, y2, 'g') # w값이 1
plt.plot(x, y3, 'b', linestyle='--') # w값이 2
plt.plot([0,0], [1.0, 0.0], ':') # 가운데 점선 추가
plt.title('sigmoid Function')
plt.show()

# 양상(존재여부) 범주
# 0(음성) if p < 0.5
# 1(양성) if p >= 0.5
# 결론적으로는 t>= 0 이면 sigma(t) >= 0.5 이므로 (반대는 반대로)
# 시그모이드 공식과 함께 생각하면 θ^T·x가 양수일때 1(양성 범주), 음수일때 0(음성 범주) 이라고 예측한다.