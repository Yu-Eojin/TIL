import numpy as np
import matplotlib.pyplot as plt
import cv2

#### 그리기 위한 함수 ####
def drawHoughLinesOnImg(img, houghLine):
    for line in houghLine:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rh0
            x1 = int(x0 + 1000 *(-b))
            y1 = int(y0 +1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

def drawCircle(img, circle):
    for co, i in enumerate(circle[0,:], start=1):
        cv2.circle(img, (i[0], i[1]), i[2], (255,0,255), 3 )

# 혼합
def blendImg(img, finalImg, alpha=0.7, beta=1., gamma=0.):
    return cv2.addWeighted(finalImg, alpha, img, beta, gamma)


# 1. 이미지 불러오기
image = cv2.imread('tictacto.png')

#2. grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# 3. 가우시안 블러 적용
blurredImg = cv2.GaussianBlur(gray_img, (5,5), 0)
edgeImg = cv2.Canny(blurredImg, 50, 120)

# 4. Detect points that from a line
dis_reso = 1
theta = np.pi / 180
threshold = 170

houghLine = cv2.HoughLines(edgeImg, dis_reso, theta, threshold)
circles = cv2.HoughCircles(blurredImg, method=cv2.HOUGH_GRADIENT, dp=0.7, minDist=12, 
                            param1=70, param2=80)

# 5. Creat empty image
houghImg = np.zeros_like(image)

drawHoughLinesOnImg(houghImg, houghLine)
drawCircle(houghImg, circles)

originalImgWithHough = blendImg(houghImg, image)


cv2.imshow('test', gray_img)
cv2.waitKey(0)