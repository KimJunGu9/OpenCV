import cv2
import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt
import skimage

img = skimage.data.coffee()
cv.imshow('Coffee image', cv.cvtColor(img, cv.COLOR_RGB2BGR))


slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=600)
# compactness : 슈퍼 화소의 모양을 조절(값이 클수록 네모에 가까운 모양이
#               만들어지는 대신 슈퍼 화소의 색상 균일성은 희생됨)
# n_segments : 슈퍼화소의 개수
sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
sp_img1 = np.uint8(sp_img1 * 255.0)
# 0~1 사이의 실수로 표현된 sp_img1을 0~255사이로 바꾸고 uint8형으로 변환


slic2 = skimage.segmentation.slic(img, compactness=40, n_segments=600)
sp_img2 = skimage.segmentation.mark_boundaries(img, slic2)
sp_img2 = np.uint8(sp_img2 * 255.0)


cv.imshow('Super pixels (compact 20)', cv.cvtColor(sp_img1, cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40)', cv.cvtColor(sp_img2, cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()