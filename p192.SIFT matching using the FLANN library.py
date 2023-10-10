import cv2 as cv
import numpy as np
import time


img1 = cv.imread('mot_color70.jpg')[190 : 350, 440 : 560] # 버스를 크롭하여 모델 영상으로 사용
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

img2 = cv.imread('mot_color83.jpg') # 장면 영상
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)


sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None) # kp1,des1,kp2,des2 두 영상 각각에서 SIFT특징점을 검출하고 기술자를 추출

print('특징점 갯수 : ', len(kp1), len(kp2))


start = time.time()
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
knn_match = flann_matcher.knnMatch(des1, des2, 2)


T = 0.7
good_match = []

for nearest1, nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance) < T:
        good_match.append(nearest1)  # 최근접 이웃 거리 비율 전략을 적용하여 좋은 쌍을 골라냄

print('매칭에 걸린 시간 : ', time.time()-start)


img_match=np.empty((max(img1.shape[0],img2.shape[0]),img1.shape[1]+img2.shape[1],3),dtype=np.uint8)
cv.drawMatches(img1,kp1,img2,kp2,good_match,img_match,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# 두 줄은 매칭 결과를 보여줄 영상을 만듦
# 35행은 두 영상을 나란히 배치하는 데 쓸 배열 img_match를 생성
# 36행은 두 영상에 특징점을 표시하고 good_match가 가진 좋은 매칭 쌍을 선으로 연결하여 표시

cv.imshow('Good Matches', img_match)

k=cv.waitKey()
cv.destroyAllWindows()