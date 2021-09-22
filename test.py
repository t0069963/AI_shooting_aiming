import cv2
import numpy as np
import mediapipe as mp
import time
import mss
import pyautogui
import pydirectinput
from PIL import ImageGrab
from PIL import Image
import win32api
import win32con
print("Ready!")
time.sleep(2)
print("GO!")
from directkeys import MouseInput

mpholistic=mp.solutions.holistic


holistic=mpholistic.Holistic()

img=ImageGrab.grab()
width = img.size[0]   # 取得寬度
height = img.size[1]   # 取得高度
sct=mss.mss()
mpDraw = mp.solutions.drawing_utils#drawing_utils繪製點工具 

pTime = 0#現在時間
cTime = 0
monitor = {"top": 0, "left": 0, "width": width, "height": height}
while True:
    interrupt = cv2.waitKey(10)
    img=np.array(sct.grab(monitor))
    img = cv2.resize(img, (int(width*0.5), int(height*0.5)), interpolation=cv2.INTER_AREA)
    #img = img.resize((int(width*0.5), int(height*0.5)), Image.ANTIALIAS)
    #img=np.array(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)#RGBA轉換RBG
    #image_height, image_width, _=img.shape
    
    results = holistic.process(img)
    #print(results.multi_hand_landmarks)
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)

            #把鼻子的點畫出來   
            if id==0:
                #cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度

                cv2.circle(img, (cx,cy),10,(255,0,255),cv2.FILLED)
                
                #pyautogui.moveTo(cx*2,cy*2,duration=0.5)                
                #pyautogui.keyDown("S")
                xloc, yloc = pyautogui.position()
                #print("aaa",cx*2,cy*2)
                #print("BBB",xloc,yloc, end='\r', flush= STrue)
                print("目標",cx*2,cy*2)
                print("目前座標",xloc,yloc)
                yyy=cy*2-yloc
                xxx=cx*2-xloc
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,xxx, yyy, 200,200)
      
        mpDraw.draw_landmarks(img, results.pose_landmarks)
#################################################################################################        
    cTime = time.time()#現在時間
    fps = 1/(cTime-pTime)
    pTime = cTime
    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0), 3)    
#################################################################################################        
    cv2.imshow('My Image', img)
    if interrupt & 0xFF == ord('q'): # 觸及小寫q，關閉視窗
        break
cv2.destroyAllWindows()
#input()