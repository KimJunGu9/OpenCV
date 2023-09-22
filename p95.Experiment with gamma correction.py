import cv2
import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.25, fy=0.25)
# 여러 장을 가로로 이어 붙여 표시할 목적으로 영상을 1/4로 축소


def gamma(f, gamma=1.0):
    f1 = f/255.0 # L = 256이라고 가정
    return np.uint8(255*(f1 ** gamma))
# f : 감마 보정할 영상
# L = 256이라고 가정하고 255.0으로 나누어 [0,1]범위의 영상으로 정규화

gc = np.hstack((gamma(img, 0.5), gamma(img, 0.75), gamma(img, 1.0),
                gamma(img, 2.0), gamma(img, 3.0)))
# hstack : 이어붙임

cv.imshow('gamma', gc)

cv.waitKey()
cv.destroyAllWindows()