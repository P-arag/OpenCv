import cv2 as cv
import numpy as np
img = cv.imread('./Resources/Elon1.jpg')
imgResized = cv.resize(img, (1000, 100))
# Height comes first then the width
imgCropped = img[0:100, 1:100]
print(imgResized.shape)
cv.imshow('Image', img)
cv.imshow('Resized Image', imgResized)
cv.imshow('Cropped Image', imgCropped)
cv.waitKey(0)
