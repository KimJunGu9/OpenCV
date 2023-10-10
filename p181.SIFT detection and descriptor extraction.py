import cv2 as cv


img = cv.imread('mot_color70.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)


sift = cv.SIFT_create() # SIFT_create 함수를 호출하여 SIFT특징점을 추출하는 데 쓸 sift객체를 생성
kp, des = sift.detectAndCompute(gray, None) # sift객체의 detectAndCompute함수를 호출하여 특징점과 기술자를 찾아 각각 kp와 des객체에 저장

gray = cv.drawKeypoints(gray, kp, None, flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# drawKeypoints 함수로 검출한 특징점을 영사엥 표시함
cv.imshow('sift', gray)

k = cv.waitKey()
cv.destroyAllWindows()