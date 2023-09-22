import cv2
import numpy as np
import sys
import cv2 as cv


img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')


cv.imshow('original_RGB', img)
cv.imshow('Upper left half', img[0:img.shape[0]//2,
                             0:img.shape[1]//2,
                             :])
cv.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4,
                         img.shape[1]//4:3*img.shape[1]//4,
                         :])
# //는 나눗셈의 몫을 구하는 연산자



cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()
