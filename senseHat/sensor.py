import time
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

print("Logging..")

while uninterrupted:
    
    

    print("{:.4f}".format(sense.humidity),"{:.4f}".format(sense.temp),"{:.4f}".format(sense.get_temperature_from_humidity()),
          "{:.4f}".format(sense.get_temperature_from_pressure()),"{:.4f}".format(sense.get_pressure()),sep=',',file=open("/home/pi/i/senseHat/senseLog.csv","a"))
    time.sleep(10)




