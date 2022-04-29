import cv2
from PIL import Image
import numpy as np
import os
import subprocess
import time

subprocess.call('v4l2-ctl -v width=1920,height=1080,pixelformat=BGR3',shell=True)
os.system("v4l2-ctl -v width=1920,height=1080,pixelformat=BGR3")
cam_read = cv2.VideoCapture(0,cv2.CAP_V4L2)
#os.system("v4l2-ctl -v width=1920,height=1080,pixelformat=BGR3")
#cam_read.set(cv2.CAP_PROP_FPS, 90)
#cam_read.set(cv2.CAP_PROP_FRAME_WIDTH, 1640)
#cam_read.set(cv2.CAP_PROP_FRAME_HEIGHT, 922)
ret, frame = cam_read.read()
subprocess.call('v4l2-ctl -v width=1920,height=1080,pixelformat=BGR3',shell=True)import v4
#time.sleep(5)
ret,frame=cam_read.read()
subprocess.call('v4l2-ctl -v width=1920,height=1080,pixelformat=BGR3',shell=True)
img = np.array(frame)
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(np.max(img),np.max(grey),grey.shape)
cam_read.release()
#cv2.imwrite("/home/pi/i/test.png",img)
#im = Image.open("/home/pi/i/test.png")
#print(list(im.getdata()),file = open("sample.txt",'w'))
#print("done")
#lst = []
#for i in range(922):
    #for j in range(1640):
        #if grey[i][j] > 60:
            #lst.append((i,j))
#print(lst,file = open("sample.txt",'w'))
#print('done')