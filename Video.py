import cv2 as cv
# Now to import a video
vid = cv.VideoCapture('./Wildlife.wmv')
while True:
    success, vidImages = vid.read()
    cv.imshow("Wildlife", vidImages)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break
    print(success)
cv.waitKey(0)
