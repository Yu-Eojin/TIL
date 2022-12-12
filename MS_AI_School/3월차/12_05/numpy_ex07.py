import numpy as np
array1 = np.arange(0, 10)
array2 = array1.copy()
array2[0] = 99
print(array1)
print(array2)
'''
결과
[0 1 2 3 4 5 6 7 8 9]
[99  1  2  3  4  5  6  7  8  9]
'''
print('-'*30)
#numpy 중복된 원소 제거
array = np.array([1,2,3,1,2,4,3,4,5])
print('중복처리 전 ', array)
print('중복 처리 후 ', np.unique(array))
'''
결과 
중복처리 전  [1 2 3 1 2 4 3 4 5]
중복 처리 후  [1 2 3 4 5]
'''
print('-'*30)
#np.isin() 내가 찾는 값이 있는지 여부를 각 인덱스 위치에 ture/false로 반환
array = np.array([1,2,3,4,5,6,7])
iwantit = np.array([1,2,3,10])
print(np.isin(array, iwantit))
'''
결과
[ True  True  True False False False False]  
'''
