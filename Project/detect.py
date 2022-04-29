import os
import time
from configparser import ConfigParser
import numpy as np
import cv2
from datetime import datetime


local_path = os.path.dirname(os.path.abspath(__file__))
cfg = ConfigParser()
cfg.read(local_path + '/config.ini')
path = cfg.get('UserPath', 'save_results_path')
test_value = cfg.get('Test', 'test_value')
threshold = cfg.get('Test', 'default_threshold')
cam_number = cfg.get('Cam', 'selected_cam')
fullFrame = cfg.get('FullFrames', 'FullResolution')

def samples_path():
    path_exist = os.path.isdir(path)
    if path_exist is False:
        print("Path does not exist")
        time.sleep(2)
        exit()


samples_path()

lowThresh = 0
def calibration():
    os.system("reset")
    print("Calibration...")
    cam_read = cv2.VideoCapture(int(cam_number))
    test_number = 0
    max_value = []
    new_x = 0
    new_y = 1
    time.sleep(2)

    while test_number < int(test_value):
        try:
            test_number += 1
            return_value, image = cam_read.read()
            test_data = np.array(image)
            test_data_crop = test_data[new_x + 10:new_x - 10, new_y + 10:new_y - 10]
            max_value.append(np.max(test_data_crop))
#             if max_value[-1] > int(threshold):
#                 detect()
            print('\r', "Test no.:", test_number, "/", test_value,
                  "Max:", np.max(test_data_crop),
                  "Average:", round(np.average(test_data_crop), 4),
                  "Exit ctrl+c", end='')
            print(test_data_crop.shape)
            time.sleep(1)

        except KeyboardInterrupt:
            cam_read.release()
            exit()
    print('\n')
    print("Calibration completed")
    avg_max_value = (sum(max_value) / len(max_value))
    print("\n")
    print("Maximum value: " + str(max(max_value)))
    print("Average of maximum values: " + str(avg_max_value))
    print("\n")
    
    indexes = []
    for index in range(len(max_value)):
        if abs(max_value[index] - avg_max_value) > 13:
            indexes.append(index)
    for i in indexes:
        del max_value[i]
    print("Maximum value: " + str(max(max_value)))
    print("\n")
    lowThresh = max(max_value)
    print(lowThresh)
    time.sleep(2)
    
calibration()
    
def start_detection():
    cam_read = cv2.VideoCapture(int(cam_number))
    sample_number = sample_save = 0
    print("Start sampling...")
    time.sleep(2)
    os.system("reset")
    while True:
        try:
            time_dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
            sample_number += 1
            ret, frame = cam_read.read()
            data = np.array(frame)
            print('\r', "Sample:", sample_number, "|", "Saved", sample_save, "|", "Press Ctrl + c to exit",np.max(data), end='')
            time.sleep(0.000001)
            counter = 0
            xy_coordinates = []
            unique = ()
            if np.max(data) >= int(threshold):
                xy = np.unravel_index(list(range(int(threshold),np.max(data)+1)),data.shape)
                zipped = list(zip(xy[1],xy[0]))
                zipped = list(set(zipped))
                zipped.sort()
                saved = ()
                print(zipped,np.max(data),sep=',',file=open(str(path)+"/debug1.txt","a"))
                while counter < len(zipped):
                    if len(zipped) == 1:
                        xy_coordinates.append(zipped[0])
                        break
                    elif counter == 0:
                        xy_coordinates.append(zipped[counter])
                        counter += 1
                        saved = zipped[0]
                    elif zipped[counter][0] - 10 < saved[0]:
                        counter += 1
                    else:
                        xy_coordinates.append(zipped[counter])
                        saved = zipped[counter]
                        counter += 1
                print(xy_coordinates,sep=',',file=open(str(path)+"/debug2.txt","a"))
                multi_detection = 0
        
                for x, y in xy_coordinates:
                    if x >= 11 and y >= 11:
                        img_crop = frame[y-10:y + 10,x-10:x + 10]
                        print(img_crop.shape,x,y,sep=',',file=open(str(path)+"/debug.txt","a"))
                        sample_save = sample_save + 1
                        if img_crop is None:
                            pass
                        else:
                            img_crop = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
                            print(img_crop.shape)
                            ret,thresh4 = cv2.threshold(img_crop,lowThresh,255,cv2.THRESH_TOZERO)
                            assert ret
                            print(time_dat, sample_number, x, y,round(np.average(data), 4), np.max(data),sep=',', file=open(str(path) + "/Report.txt", "a"))
                            img_zoom = cv2.resize(thresh4, (40,40), interpolation=cv2.INTER_CUBIC)
                            #gray_img_zoom = cv2.cvtColor(img_zoom, cv2.COLOR_BGR2GRAY)
                            cv2.imwrite(str(path) + "/" + str(time_dat) +
                                        " Sample no. %i:%i.png" % (sample_number,multi_detection), img_zoom)
                        multi_detection += 1
        except KeyboardInterrupt:
            cam_read.release()
            exit()

start_detection()