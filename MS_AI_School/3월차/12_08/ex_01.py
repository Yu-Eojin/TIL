# 같은 크기의 이미지 블렌딩 실험
import cv2
import matplotlib.pyplot as plt
import numpy as np

large_img = cv2.imread('./image.png')
watermark = cv2.imread('./logo.png')

print('large image size >> ', large_img.shape)
print('watermark size >> ', watermark.shape)

print('-' * 30)

img1 = cv2.resize(large_img, (800,600))
img2 = cv2.resize(watermark, (800,600))

print('large image size resized >> ', img1.shape)
print('watermark size resized >> ', img2.shape)

### 혼합진행 

# 베이스 5:5
blend = cv2.addWeighted(img1,0.5, img2,0.5, 0)

# 9:1
blend = cv2.addWeighted(img1,0.9, img2,0.1, 0)

# 1로 설정
blend = cv2.addWeighted(img1,1, img2,1, 0)
cv2.imshow('blended', blend)

# cv2.imshow('image', img1)
# cv2.imshow('watermark', img2)
cv2.waitKey(0)

