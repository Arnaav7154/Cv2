import cv2
img =cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    success,img = img.read()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces= face_cascade.detectMultiScale(gray,1.2,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
    cv2.imshow("frame",img)
    cv2.waitKey(0)