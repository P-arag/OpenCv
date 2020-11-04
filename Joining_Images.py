import cv2 as cv
import numpy as np
img = cv.imread('./Resources/Elon1.jpg')
horizontallyStackedImg = np.hstack((img, img))
verticallyStackedImg = np.vstack((img, img))
cv.imshow("Elon Musk Hor", horizontallyStackedImg)
cv.imshow("Elon Musk Ver", verticallyStackedImg)
cv.waitKey(0)
