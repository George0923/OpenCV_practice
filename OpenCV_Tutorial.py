import cv2


#讀取圖片
"""
img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)        #調整大小  (調整像素) or 以倍數調整
cv2.imshow('img', img)
cv2.waitKey(0)     #開啟後等待多久 (單位:毫秒) => 0=無限久直到手動or按任意鍵關閉
"""

#讀取影片
"""
cap = cv2.VideoCapture('thumb.mp4')
while True:
    ret, frame = cap.read()        #會回傳兩個值 =>(True/False, 畫面的下一針)
    if ret:
        frame = cv2.resize(frame, (0,0), fx = 0.4, fy = 0.4)
        cv2.imshow('video', frame)
    else:
        break
    #cv2.waitKey(10)   #每取得一針等...毫秒  => 針數越高影片越慢  反之亦然
    if cv2.waitKey(10) == ord('q'):  #按q時 => 程式結束
        break
"""

#讀取 電腦視訊鏡頭

camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()        #會回傳兩個值 =>(True/False, 畫面的下一針)
    if ret:
        frame = cv2.resize(frame, (0,0), fx = 1.2, fy = 1.2)
        cv2.imshow('video', frame)
    else:
        break
    #cv2.waitKey(10)   #每取得一針等...毫秒  => 針數越高影片越慢  反之亦然
    if cv2.waitKey(10) == ord('q'):  #按q時 => 程式結束
        break
