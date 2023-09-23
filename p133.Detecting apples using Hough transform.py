import cv2
import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('apples.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 100, 
                         param1=150, param2=20, minRadius=50, maxRadius=120)
# 
# cv.HOUGH_GRADIENT : 에지 방향 정보를 추가로 사용하는 방법
# 1 : 누적 배열의 크기를 지정하는데 1로 설정하면 입력 영상과 같은 크기를 사용
# 100 : 원 사이의 최소 거리를 지정하는데 작을수록 많은 원이 검출
# param1=150 : 캐니 에지 알고리즘이 사용하는 T-high
# param2=20 : 비최대 억제를 적용할 때 쓰는 임계값
# minRadius=50 : 원의 최소 반지름
# maxRadius=120 : 원의 최대 반지름


for i in apples[0]:
    cv.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 2)

cv.imshow('Apple detection', img)

cv.waitKey()
cv.destroyAllWindows()