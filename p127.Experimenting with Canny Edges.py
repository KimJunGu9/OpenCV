import cv2
import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('soccer.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


canny1 = cv.Canny(gray, 50, 150) # T-low = 50, T-hight = 150 으로 설정
canny2 = cv.Canny(gray, 100, 100) # T-low = 100, T-hight = 200 으로 설정


cv.imshow('Original', gray)
cv.imshow('Canny1', canny1)
cv.imshow('Canny2', canny2)


cv.waitKey()
cv.destroyAllWindows()