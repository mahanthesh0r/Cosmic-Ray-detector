import numpy as np
import cv2
import time
from fractions import Fraction
from picamera import PiCamera
from picamera.array import PiRGBArray
#from parameters import setparams
import os
import signal
import picamera.array
from io import BytesIO


def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def setparams(c):
    c.led = False
    c.awb_mode ='off' #auto white balance
    c.awb_gains = 1 # 0.0...8.0  (red,blue)
    c.resolution = (3264,2464)
    c.exposure_mode = 'off'
    c.iso= 800
    c.framerate = 17
    c.shutter_speed = 1000000//17
    time.sleep(2)
    c.drc_strength = 'off'
    c.image_denoise = False
    c.image_effect = 'none'
#cam = cv2.VideoCapture(0)
interrupted = False
camera = PiCamera()
#camera.framerate = 17
setparams(camera)
signal.signal(signal.SIGINT, signal_handler)
stream = PiRGBArray(camera)
f = 0
time.sleep(2)
start = time.time()
for frame in camera.capture_continuous(stream,format='rgb',use_video_port=True):
    f+=1
    #ret,frame = cam.read()
    #fram.seek(0)
    #frame = camera.capture(stream,"rgb")
    #print(frame.shape)
    data = frame.array
    #print('Max:',np.max(data),'Non zero',np.count_nonzero(data),data.shape)
    stream.seek(0)
    stream.truncate()
    if interrupted:
        print(f/(time.time()-start),time.time()-start)
        #cam.release()
        camera.close()
        break
        
    
    
    
    
    
    
    
    

