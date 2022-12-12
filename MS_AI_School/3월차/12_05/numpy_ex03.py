# Numpy 가장 많이 사용되는 함수
# 1. 원소 정렬
import numpy as np

array = np.array([15,20,5,12,7])
np.save('./array.npy', array)
array_data = np.load('./array.npy')
array_data.sort()
print('오름차순', array_data)

print('내림차순', array_data[::-1])
'''
결과
오름차순 [ 5  7 12 15 20]
내림차순 [20 15 12  7  5]
'''
