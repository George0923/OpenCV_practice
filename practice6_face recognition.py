import cv2

img = cv2.imread('lenna.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 5)     #顏色, (單次)縮放比例, 最少框到幾次才算偵測到的次數=>數字越大檢測得越嚴謹
print(len(faceRect)) 


for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0), 2)



cv2.imshow('img', img)
cv2.waitKey(0)