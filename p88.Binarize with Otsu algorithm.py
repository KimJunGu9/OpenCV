import cv2
import numpy as np
import sys
import cv2 as cv


img = cv.imread('soccer.jpg')

t, bin_img = cv.threshold(img[:,:,2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# 0, 255 : 명암값의 범위
# cv.THRESH_BINARY+cv.THRESH_OTSU : 오츄알고리즘으로 이진화를 수행

print('오츄 알고리즘이 찾은 최적 임계값 = ', t)


cv.imshow('R channel', img[:,:,2]) # R 채널 영상
cv.imshow('R channel binarization', bin_img) # R 채널 이진화 영상

cv.waitKey()
cv.destroyAllWindows()