import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands (self.mode, self.maxHands, self.detectionCon, self.trackCon)

        # Function to draw line between 2 points
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4,8,12,16,20]

        
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor (img, cv2.COLOR_RGB2BGR)
        self.results = self.hands.process (imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                # pass the original img / below line shoud give me point on hand
                # mpDraw.draw_landmarks(img, handLms)
                if draw:
                    self.mpDraw.draw_landmarks (img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img
    def findPosition(self,img,handNo = 0 ,draw= True):

        self.lmList= []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate (myHand.landmark):
         # this will give you the x,y cordnation by ratio so multiple it by width and height / print(id,lm)
                #print("Print id,lm",id, lm)
                h, w, c = img.shape
                cx, cy = int (lm.x * w), int (lm.y * h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle (img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return self.lmList

# to check if it is detecting any thing print(results.multi_hand_landmarks)
    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1) # açık oldugunda
            else:
                fingers.append(0) # kapalı oldugunda
        return fingers

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPostion(img)
        if len(lmList)!= 0:
            print("Postion of Lslist[x]",lmList[0])
        # Capturing FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # showing as in the screen
        cv2.putText (img, str (int (fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow ("img", img)
        cv2.waitKey (1)


if __name__ == "__main__":
    main()
