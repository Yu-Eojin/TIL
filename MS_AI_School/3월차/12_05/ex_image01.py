import cv2

img_path = './cat.png'
img = cv2.imread(img_path)

h, w, _ = img.shape

print('이미지 타입 : ', type(img))
print(f'이미지 높이 {h}, 이미지 넓이 {w}')
'''
결과
이미지 타입 :  <class 'numpy.ndarray'>
이미지 높이 1080, 이미지 넓이 1920
'''

cv2.imshow('image', img)
cv2.waitKey(0)

