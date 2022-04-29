import cv2
from datetime import datetime
import copy
import numpy as np

import imutils

def hit_detection(img):
    print(img.shape)
    hit_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    pos = np.unravel_index(img.argmax(),img.shape)
    bilateral = cv2.bilateralFilter(img, 3, 3, 3)
    edges = cv2.Canny(bilateral, 35, 60)
    contours = cv2.findContours(copy.deepcopy(edges), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    st = set()
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            st.add((cX,cY))
    multi_detection = 0
    for coordinates in st:
        img_crop = img[coordinates[1]-20:coordinates[1]+20,coordinates[0]-20:coordinates[0]+20]
        print(img_crop.shape)
        if img_crop.shape[0] == 40 and img_crop.shape[1] == 40:
            multi_detection += 1
            cv2.imwrite("/home/pi/i/PiCamera/OpenCV/test/"+str(hit_time)+str(multi_detection)+".png",img_crop)
    #cv2.imwrite("/home/pi/i/PiCamera/"+str(hit_time)+"1.png",img)
    print(multi_detection)
    print(st,pos,sep=',', file=open("/home/pi/i/report.txt","a"))
    
