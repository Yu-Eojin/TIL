import numpy as np
import cv2

# 이미지 경로
x = cv2.imread('./cat.png', 0) # 흑백이미지
y = cv2.imread('./cat.png', 1) # 컬러이미지

cv2.imshow('image show gray', x)
cv2.imshow('image show', y)
cv2.waitKey(0)

# 여러개 파일 save
np.savez('./image.npz', array1=x, array2=y)

# 압축방법
np.savez_compressed('./image_compressed.npz',array1=x,array2=y)

# npz 데이터 로드
data = np.load('./image_compressed.npz')

result1 = data['array1']
result1 = data['array1']

cv2.imshow('result01', result1)
cv2.waitKey(0)