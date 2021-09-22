import cv2
import numpy as np
import mediapipe as mp
import time
from PIL import ImageGrab
from PIL import Image
print("Ready!")
time.sleep(2)
print("GO!")

mpholistic=mp.solutions.holistic


holistic=mpholistic.Holistic()


mpDraw = mp.solutions.drawing_utils#drawing_utils繪製點工具 

pTime = 0#現在時間
cTime = 0

while True:
    interrupt = cv2.waitKey(10)
    img=ImageGrab.grab()
    width = img.size[0]   # 取得寬度
    height = img.size[1]   # 取得高度
    img = img.resize((int(width*0.5), int(height*0.5)), Image.ANTIALIAS)
    img=np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#轉換RBG
    image_height, image_width, _=img.shape
    results = holistic.process(img)
    #print(results.multi_hand_landmarks)
    if results.pose_landmarks:
        xx=int(results.pose_landmarks.landmark[13].x*image_width)
        yy=int(results.pose_landmarks.landmark[13].x*image_height)
        print(results.pose_landmarks.landmark[13].x*image_width) 
      #print(
          #f'Nose coordinates: ('
          #f'{results.pose_landmarks.landmark[mpholistic.PoseLandmark.NOSE].x * image_width}, '
          #f'{results.pose_landmarks.landmark[mpholistic.PoseLandmark.NOSE].y * image_height})'
      #)
        #cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度
        cv2.circle(img, (xx,yy),10,(255,0,255),cv2.FILLED)
        mpDraw.draw_landmarks(img, results.pose_landmarks)
    cTime = time.time()#現在時間
    fps = 1/(cTime-pTime)
    pTime = cTime
    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0), 3)    
        
    #qcv2.resizeWindow('My Image', image_width//4, image_height//4) # resize window
    cv2.imshow('My Image', img)
    if interrupt & 0xFF == ord('q'): # 觸及小寫q，關閉視窗
      break
cv2.destroyAllWindows()
#input()