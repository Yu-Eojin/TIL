import numpy as np
# 실행마다 결과 동일
# 랜덤한 값이 실행할 때 마다 변경되지 않도록 Seed를 만든다
np.random.seed(777)
print(np.random.randint(0,10,(2,3)))