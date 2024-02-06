import cv2
import numpy as np
import random


"""
img = cv2.imread('colorcolor.jpg')
#print(type(img))
print(img.shape)        #得知圖片的維度

"""    
""" 圖片維度顯示意思
[
    [[0,255,0], [0,255,0], [0,0,255], ........ 700張]
    [[...], [...], [...].........[...]]
    [[...], [...], [...].........[...]],
    ....1015
]
"""

#創建一個自己的圖片
"""
img = np.empty((300, 300, 3), np.uint8)     
for row in range(300):
    for col in range(300):
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow('img', img)
cv2.waitKey(0)
"""


"""
img = cv2.imread('colorcolor.jpg')
for row in range(300):
    for col in range(img.shape[1]):
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow('img', img)
cv2.waitKey(0)
"""

#切割圖片
"""
img = cv2.imread('colorcolor.jpg')
newimg = img[:150, :200]
cv2.imshow('img', img)
cv2.imshow('newimg', newimg)
cv2.waitKey(0)
"""