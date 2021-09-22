import numpy as np
import cv2
import mss
import time
import pydirectinput
import pyautogui
import win32api
import win32con
from PIL import ImageGrab

# 載入分類器
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)#cv2.CAP_DSHOW微軟特有

img=ImageGrab.grab()
width = img.size[0]   # 取得寬度
height = img.size[1]   # 取得高度
pTime = 0#現在時間
cTime = 0
monitor = {"top": 0, "left": 0, "width": width, "height": height}
sct=mss.mss()
print("Ready!")
time.sleep(2)
print("GO!")
while True:
    interrupt = cv2.waitKey(10)
    img=np.array(sct.grab(monitor))
    img = cv2.resize(img, (int(width*0.5), int(height*0.5)), interpolation=cv2.INTER_AREA)
    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# 轉成灰階    
    
    bodys = body_cascade.detectMultiScale(gray,scaleFactor=1.12,minNeighbors=3)# 偵測    
    
    for (x, y, w, h) in bodys:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)# 繪製方框
        cx=x+(w//2)
        cy=y+(h//2)
        cv2.circle(img, (cx,cy),10,(255,0,255),cv2.FILLED)
        xloc, yloc = pyautogui.position()
        #print("目標",cx*2,cy*2)
        #print("目前座標",xloc,yloc)
        xxx=(cx*2)-xloc
        yyy=(cy*2)-yloc
        #print("偏移",xxx,yyy)
        #pyautogui.moveTo(cx*2,cy*2,duration=0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,xxx//2, yyy//2, 200,200)
        time.sleep(1)
        xloc, yloc = pyautogui.position()
        #print(xloc,yloc)
      
        #print("1")
        #continue
    #break
    
    
#################################################################################################        
    cTime = time.time()#現在時間
    fps = 1/(cTime-pTime)
    pTime = cTime
    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0), 3)    
#################################################################################################        

    cv2.imshow("Webcam", img) # 顯示鏡頭畫面
    #計算找到多少        
    if interrupt & 0xFF == ord('q'): # 觸及小寫q，關閉webcam
      break
      
cap.release()
cv2.destroyAllWindows()