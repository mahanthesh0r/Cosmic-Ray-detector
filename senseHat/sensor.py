import time
import datetime
import signal
import os
from sense_hat import SenseHat


def signal_handler(signal, frame):
    global uninterrupted
    uninterrupted = False

uninterrupted = True
signal.signal(signal.SIGINT, signal_handler)
os.system("reset")


start = time.time()
sense = SenseHat()
sense.set_imu_config(True, True, True)

print("Logging..")

while uninterrupted:
    
    

    print(datetime.datetime.now(),
          "{:.4f}".format(sense.humidity),
          "{:.4f}".format(sense.temp),
          "{:.4f}".format(sense.get_temperature_from_humidity()),
          "{:.4f}".format(sense.get_temperature_from_pressure()),
          "{:.4f}".format(sense.get_pressure()),
          "{:.4f}".format(sense.orientation_radians["pitch"]),
          "{:.4f}".format(sense.orientation_radians["roll"]),
          "{:.4f}".format(sense.orientation_radians["yaw"]),
          "{:.4f}".format(sense.compass),
          "{:.4f}".format(sense.compass_raw["x"]),
          "{:.4f}".format(sense.compass_raw["y"]),
          "{:.4f}".format(sense.compass_raw["z"]),
          "{:.4f}".format(sense.gyro["pitch"]),
          "{:.4f}".format(sense.gyro["roll"]),
          "{:.4f}".format(sense.gyro["yaw"]),
          "{:.4f}".format(sense.accel["pitch"]),
          "{:.4f}".format(sense.accel["roll"]),
          "{:.4f}".format(sense.accel["yaw"]),
          sep=',',
          file=open("/home/pi/i/senseHat/senseLog.csv","a"))
    
    
    time.sleep(10)




