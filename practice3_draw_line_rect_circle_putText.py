import cv2
import numpy as np

img = np.zeros((600,600,3), np.uint8)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (255,0,0), 2)  # => 圖片, 左上角到右下角座標位置, 顏色, 粗度 
cv2.rectangle(img, (0,0), (400,300), (0,0,255), cv2.FILLED)      #=> 圖片, 左上角點, 右下角點, 顏色, 粗度 (FILLED=>填滿)
cv2.circle(img, (300,400), 30, (0,255,0), cv2.FILLED)        #圖片, 中心點, 半徑, 顏色, 線條粗度
cv2.putText(img, "Hello there", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),2)      #圖片, 訊息, 左下角的點座標, 字體, 文字大小, 顏色, 粗度) 


cv2.imshow('img', img)
cv2.waitKey(0)