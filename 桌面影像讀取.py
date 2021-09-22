import numpy as np
import time
import mss
import cv2
from PIL import ImageGrab
print("Ready!")
time.sleep(2)
print("GO!")
pTime = 0#現在時間
cTime = 0
img=ImageGrab.grab()
width = img.size[0]   # 取得寬度
height = img.size[1]   # 取得高度
sct=mss.mss()
monitor = {"top": 0, "left": 0, "width": width, "height": height}
while True:
    interrupt = cv2.waitKey(10)
    img=np.array(sct.grab(monitor))
#################################################################################################        
    cTime = time.time()#現在時間
    fps = 1/(cTime-pTime)
    pTime = cTime
    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0), 3)    
#################################################################################################
    # 顯示圖片
    #cv2.cvtColor(img,cv2.COLOR_BGR2RGB)將img從RGB轉BGR 因為CV2是吃BGR
    cv2.imshow('My Image', img)

        

    if interrupt & 0xFF == ord('q'): # 觸及小寫q，關閉webcam
      break
cv2.destroyAllWindows()