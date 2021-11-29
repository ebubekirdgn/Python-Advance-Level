import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


#########################
wCam,hCam = 480 ,480
#########################

pTime =0
detector = htm.handDetector(detectionCon =0.7) 

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()


volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 450 
volPer = 0
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # pc kamerasının acılmasını saglar
cap.set(3,wCam)
cap.set(4,hCam)

while True:
  success , img = cap.read()
  img = detector.findHands(img)
  lmList = detector.findPosition(img, draw=False)
  if len(lmList) != 0:
      #print(lmList[4],lmList[8])
      
      x1,y1 = lmList[4][1],lmList[4][2]  # baş parmak alındı
      x2,y2 = lmList[8][1],lmList[8][2]  #işaret parmağı alındı.
      cx,cy = (x1+x2)//2 , (y1+y2)//2

      cv2.circle(img ,(x1,y1),8,(255,0,255),cv2.FILLED)
      cv2.circle(img ,(x2,y2),8,(255,0,255),cv2.FILLED)

      cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3) # iki parmak birleştirildi.
      cv2.circle(img ,(cx,cy),8,(255,0,0),cv2.FILLED)
      
      length = math.hypot(x2-x1,y2-y1) #iki parmagımızı max ne kadar acabiliyoruz ve min ne kadar kapatabiliyoruz o sayı degerlerini alıyoruz. 
      #print(length)
      
      # Hand Range 30-200
      # Volume Range 65 -0


      vol = np.interp(length,[30,260],[minVol,maxVol])
      volBar = np.interp(length,[30,260],[180,450])
      volPer = np.interp(length,[30,260],[0,100])

      print(int(length),vol)
      volume.SetMasterVolumeLevel(vol, None)



      #benimki max = 200 min = 30 cıktı o yuzden 30 den kucukse iki parmak arası uzaklık daireyi farklı renkte göster dedim.
      if length <30:
            cv2.circle(img ,(cx,cy),8,(0,255,0),cv2.FILLED)


  cv2.rectangle(img,(450,80),(180,50),(0,255,0),3)
  cv2.rectangle(img,(int(volBar),80),(180,50),(0,255,255),cv2.FILLED)
  cv2.putText(img,f'{int(volPer)} % ',(500,50),cv2.FONT_HERSHEY_PLAIN,
  2,(0,255,0),4)



  cTime = time.time()
  fps= 1 / (cTime - pTime)
  pTime = cTime

  cv2.putText(img ,f'FPS: {int(fps)}',(20,40),cv2.FONT_HERSHEY_PLAIN,
        2,(255,0,0),3)
   
  cv2.imshow("Img:",img)
  cv2.waitKey(1)