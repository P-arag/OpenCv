import cv2 as cv
import numpy as np
import time


def empty(a):
    pass


# we create a new window called trackbar
cv.namedWindow("Trackbar")
cv.resizeWindow("Trackbar", 640, 240)
cv.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv.createTrackbar("Hue Max", "Trackbar", 179, 179, empty)
cv.createTrackbar("Sat Min", "Trackbar", 89, 255, empty)
cv.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv.createTrackbar("Val Min", "Trackbar", 255, 255, empty)
cv.createTrackbar("Val Max", "Trackbar", 255, 255, empty)
##################


def separateColor(path):
    while True:
        img = cv.imread(path)
        imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        hueMin = cv.getTrackbarPos("Hue Min", "Trackbar")
        hueMax = cv.getTrackbarPos("Hue Max", "Trackbar")
        satMin = cv.getTrackbarPos("Sat Min", "Trackbar")
        satMax = cv.getTrackbarPos("Sat Max", "Trackbar")
        valMin = cv.getTrackbarPos("Val Min", "Trackbar")
        valMax = cv.getTrackbarPos("Val Max", "Trackbar")
        lower = np.array([hueMin, satMin, satMin])
        upper = np.array([hueMax, satMax, valMax])
        maskedHSV = cv.inRange(imgHSV, lower, upper)
        imgResult = cv.bitwise_and(img, img, mask=maskedHSV)
        horizontallyStackedImage = np.hstack((img, imgResult))
        #########
        cv.imshow('All Images', horizontallyStackedImage)

        cv.waitKey(1)


separateColor('./Resources/Elon1.jpg')
