import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Elon1.jpg')
faceCascade = cv.CascadeClassifier('./Cascades/haarcascade_frontalface_default.xml')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 2)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow("Result", img)
cv.waitKey(0)
