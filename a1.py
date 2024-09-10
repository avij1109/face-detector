import cv2

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#choose an image to detect faces in
img = cv2.imread('rdj.png')

cv2.imshow('clever programmer face detector', img)
cv2.waitKey()

print("done")