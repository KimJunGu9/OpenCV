import cv2
import numpy as np
import sys
import cv2 as cv


img = cv2.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')


def draw(event,x,y,flags,param): # 콜백 함수
    if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭했을때
        cv.rectangle(img,(x,y),(x + 200, y + 200), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN: # 마우스 오른쪽 버튼 클릭했을때
        cv.rectangle(img,(x,y),(x + 100, y + 100), (255, 0, 0), 2)

    cv.imshow('Drawing',img)


cv.namedWindow('Drawing')
cv.imshow('Drawing',img)


cv.setMouseCallback('Drawing',draw) # Drawing 윈도우가 draw 콜백 함수 지정
# 'Drawing'이라는 이름의 윈도우에서 마우스 이벤트가 발생하면 draw라는 콜백함수를 호출하라고 등록한다.

while(True): # 마우스 이벤트가 언제 발생할지 모르므로 무한 반복
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break