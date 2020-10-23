import cv2 as cv
# This is how we import an image
img = cv.imread('./Elon1.jpg')
cv.imshow('Elon Musk', img)
cv.waitKey(0)
