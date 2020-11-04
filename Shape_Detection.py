import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Shapes.png')
imgContours = img.copy()
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)


def getContours(image):
    # cv.RETR_EXTERNAL
    contours, heiarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        print(area)
        if area > 500:
            cv.drawContours(imgContours, contour, -1, (255, 0, 0), 3)
            perimeter = cv.arcLength(contour, True)
            # print(perimeter)
            cornerPointsApprox = cv.approxPolyDP(contour, 0.03 * perimeter, True)
            print(len(cornerPointsApprox))
            x, y, w, h = cv.boundingRect(cornerPointsApprox)
            corners = len(cornerPointsApprox)
            cv.rectangle(imgContours, (x, y), (x + w, y + h), (56, 12, 245), 3)
            if corners == 3:
                cv.putText(imgContours, "Triangle", (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
            if corners == 4:
                cv.putText(imgContours, "Quadrilateral", (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
            if corners > 4:
                cv.putText(imgContours, "Circle", (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)


getContours(imgCanny)
stackedImgs = np.hstack((imgBlur, imgCanny))
cv.imshow("Shapes", stackedImgs)
cv.imshow("Contours", imgContours)
cv.waitKey(0)
