import cv2
import numpy as np
import sys
import cv2 as cv


img = cv2.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')


def draw(event,x,y,flags,param):
    global ix, iy # 버튼을 클릭한 순간의 좌표를 저장할 ix, iy를 전역변수로 선언

    if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
        ix, iy = x, y # 클릭하면 좌표 x와 y를 전역변수 ix, iy에 저장
    elif event == cv.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼을 클릭했을 때 직사각형 그리기
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2) 
        # 버튼을 놓으면 클릭했을때 저장해둔 좌표(ix,iy)와 놓았을때 좌표(x,y)를 이용해 직사각형 그린다




    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while (True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break