import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, cam = cap.read()

    if(ret) :
        cv.imshow('camera', cam)

        if cv.waitKey(1) & 0xFF == 27: # esc키를 누르면 닫음
            break

    roi = cam[269: 795, 537: 1416]
    rows, cols, _ = roi.shape
    gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    gray_roi = cv.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv.threshold(gray_roi, 3, 255, cv.THRESH_BINARY_INV)
    _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv.boundingRect(cnt)

        # cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
        break

    cv.imshow("Threshold", threshold)
    cv.imshow("gray roi", gray_roi)
    cv.imshow("Roi", roi)
    key = cv.waitKey(30)
    if key == 27:
        break


cap.release()
cv.destroyAllWindows()
