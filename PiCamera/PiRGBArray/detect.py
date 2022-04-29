import cv2
from datetime import datetime
import copy
import numpy as np

def hit_detection(img,brightest_pixel,non_zero):
    hit_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    pos = np.unravel_index(img.argmax(),img.shape)
    bilateral = cv2.bilateralFilter(img, 3, 3, 3)
    edges = cv2.Canny(bilateral, 35, 60)
    contours = cv2.findContours(copy.deepcopy(edges), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imwrite("/home/pi/i/PiCamera/"+str(hit_time)+".png",edges)
    cv2.imwrite("/home/pi/i/PiCamera/"+str(hit_time)+"1.png",img)
    print(contours,brightest_pixel,non_zero,pos,sep=',', file=open("/home/pi/i/PiCamera/report.txt","a"))
    