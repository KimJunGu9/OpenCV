import cv2
import numpy as np
import sys
import cv2 as cv

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')


cv.rectangle(img,(830,30),(1000,200),(0,0,255),2) # 직사각형 그리기

cv2.putText(img, 'laugh', (830,24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2) # 글씨 쓰기

cv2.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()