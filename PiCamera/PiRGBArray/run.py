from picamera import PiCamera
from parameters import setparams
from detect import hit_detection
import signal
import picamera.array
import cv2
import numpy as np
import time
import os



def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    
saved = 0
interrupted = False
#camera = cv2.VideoCapture(0)
camera = PiCamera()
setparams(camera)
print(camera.framerate,camera.shutter_speed)
time.sleep(2)
signal.signal(signal.SIGINT, signal_handler)
os.system("reset")

with picamera.array.PiRGBArray(camera) as stream:
    frames = 0
    start = time.time()
    for frame in camera.capture_continuous(stream,format='rgb',use_video_port=True):
        #print(time.time()-start)
        #start = time.time()
        #print(str(time.time()-start))
        img = frame.array
        #print(img.shape)
        frames += 1
        #grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        #print(img.argmax())
        brightest_pixel = np.max(img)
        non_zero = np.count_nonzero(img)
        print('Brightest Pixel :',brightest_pixel,'Non Zero Count :',non_zero,'Saved :',saved)
        #time.sleep(0.000001)
        stream.seek(0)
        stream.truncate()
        #start = time.time()
        if brightest_pixel > 20:
            saved += 1
            hit_detection(img,brightest_pixel,non_zero)
        if interrupted:
            break
    print(frames)
    print(time.time()-start)
    print(frames/(time.time()-start))
    camera.close()
        