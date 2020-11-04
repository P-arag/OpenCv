import cv2 as cv
import numpy as np
img = cv.imread('./Resources/Elon1.jpg')
# A grayScale image
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# A blurred image
imgBlur = cv.GaussianBlur(imgGray, (11, 11), 9)
# A Canny image
imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
imgCanny = cv.Canny(imgRGB, 150, 200)
# Dilated Canny image
dilationKernel = np.ones((3, 3), np.uint8)
imgDilated = cv.dilate(imgCanny, dilationKernel, iterations=1)
# Eroded Canny Image
imgEroded = cv.erode(imgDilated, dilationKernel, iterations=1)
# All image displays
cv.imshow("Gray Scale image", imgGray)
cv.imshow("Gray Blurred Image", imgBlur)
cv.imshow("RGB Canny Image", imgCanny)
cv.imshow("Dilated Canny Image", imgDilated)
cv.imshow("Eroded Canny Image", imgEroded)
cv.waitKey(5000)
