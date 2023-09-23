import cv2
import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('soccer.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3) # 소벨 연산자 적용
# cv.CV_32F : 결과영상을 32비트 실수 맵에 저장하라고 지시
# 1, 0 : x연산자를 사용하라고 지시
# ksize=3 : 3x3크기를 사용하라고 지시

grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)
# 0, 1 : y연산자를 사용하라고 지시



sobel_x = cv.convertScaleAbs(grad_x) # 절대값을 취해 양수 영상으로 변환
sobel_y = cv.convertScaleAbs(grad_y)


edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0) # 에지 강도 계산
# sobel_x와 sobel_y에 0.5를 곱해서 더한 결과를 edge_strength에 저장

# addWeighted(img1, a, img2, b, c) : img1 x a + img2 x b + c

cv.imshow('Original', gray)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)
cv.imshow('edge strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()