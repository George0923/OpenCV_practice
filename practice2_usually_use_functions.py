import cv2
import numpy as np

kernel = np.ones((10,10), np.uint8)
kernel1 = np.ones((10,10), np.uint8)

img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)

# cvtColor
"""
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #轉換圖片顏色
cv2.imshow('gray', gray)
"""

#GaussianBlur
"""
blur = cv2.GaussianBlur(img, (7,7), 10)     # 高斯模糊 =>圖片, 核(須為基數), 標準差
cv2.imshow('blur', blur)
"""

#Canny & dilate & erode
"""
canny = cv2.Canny(img, 150, 200)        # Canny => 圖片,最低門檻, 最高門檻
cv2.imshow('canny', canny)
dilate = cv2.dilate(canny, kernel, iterations = 1)       #膨脹
cv2.imshow('dilate', dilate)
erode = cv2.erode(dilate, kernel1, iterations = 1)
cv2.imshow('erode', erode)
"""


cv2.imshow('img', img)
cv2.waitKey(0)