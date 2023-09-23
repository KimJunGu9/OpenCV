import cv2
import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('soccer.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(gray, 100, 200)


contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)


lcontour = []

for i in range(len(contour)):
    if contour[i].shape[0] > 100: # 길이가 100보다 크면
        lcontour.append(contour[i])


cv.drawContours(img, lcontour, -1, (0, 255, 0), 3)
# drawContours : 영상에 경계선을 그림
# img : 경계선을 넣을 영상
# lcontour : 경계선인데 lcontour객체로 설정
# -1 : -1로 설정하면 모든 경계선을 그려주며, 
#      양수로 설정하면 해당 번호에 해당하는 경계선 하나만 그려줌
# (0, 255, 0) : 색
# 3 : 두께

cv.imshow('Original with contours', img)
cv.imshow('Canny', canny)

cv.waitKey()
cv.destroyAllWindows()