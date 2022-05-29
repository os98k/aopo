"""
@author: Global Computers
Face Mesh Detection using OpenCV and mediapipe

"""
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector()

while True:
    success, img = cap.read()
    #cv2.imwrite("D://test.jpg", img)

    img = detector.findHands(img, draw=False)
    lmList, bbox = detector.findPosition(img, draw=False)

    if bbox:
        cvzone.cornerRect(img, bbox)

    cv2.imshow("image", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows