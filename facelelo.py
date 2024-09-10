import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

'''#choose an image to detect faces in
img = cv2.imread('rdj.png')
img = cv2.imread('download.png')'''
webcam = cv2.VideoCapture(0)

while True:
   successful_read, frame = webcam.read()
   grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   face_cordinates = trained_face_data.detectMultiScale(grayscale_img)
   for (x,y,w,h) in face_cordinates:
    cv2.rectangle(frame, (x, y), (x+w, y+h), ( randrange(256),randrange(256),randrange(256)), 2)
   cv2.imshow('clever programme detector', frame)
   key = cv2.waitKey(1)
   
   if key==81 or key==113:
     break
   

webcam.release()



'''

#rectangle
 

#print(face_cordinates)
#loading image
cv2.imshow('clever programmer face detector', frame)
cv2.waitKey()



print("done"),'''