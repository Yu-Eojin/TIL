import cv2

def image_show(image):
    cv2.imshow('show',image)
    cv2.waitKey(0)

image_path = './cat.png'

#이미지 읽기
image = cv2.imread(image_path)

# 이미지 크롭 [시작:끝:단계]
image_crop = image[100:,:400]

# 저장코드 추가
cv2.imwrite('./cat_crop.png', image_crop)

image_show(image_crop)