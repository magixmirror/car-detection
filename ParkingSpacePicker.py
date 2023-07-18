import cv2
import pickle

img = cv2.imread('carParkImg.png')

while True:
    cv2.rectangle(img, (100, 230), (200, 150), (0, 0, 255), 2)
    cv2.imshow("image", img)
    cv2.waitKey(1)