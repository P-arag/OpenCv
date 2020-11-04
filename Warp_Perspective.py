import cv2 as cv
import numpy as np
img = cv.imread('./Resources/Cards.jpg')
pts = np.float32([[188, 68], [242, 78], [161, 125], [220, 144]])
width, height = 186, 271
ptsRef = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
imgMatrix = cv.getPerspectiveTransform(pts, ptsRef)
imgOutput = cv.warpPerspective(img, imgMatrix, (width, height))
cv.imshow('Cards', img)
cv.imshow("Warped Card", imgOutput)
cv.waitKey(0)
