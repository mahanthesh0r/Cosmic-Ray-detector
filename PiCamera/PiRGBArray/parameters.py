import time
from fractions import Fraction

def setparams(c):
    c.led = False
    c.awb_mode ='off' #auto white balance
    c.awb_gains = (1,1.) # 0.0...8.0  (red,blue)
    c.resolution = (1920,1088)
    c.exposure_mode = 'off'
    c.iso= 800
    c.framerate = Fraction(1,3)
    c.shutter_speed = 3000000
    time.sleep(2)
    c.drc_strength = 'off'
    c.image_denoise = False
    c.image_effect = 'none'

def getparams(c):
    print('analog , digital gain {} , {}'.format(c.analog_gain,c.digital_gain))
    print('auto white balance {}  , AWB gains {}'.format(c.awb_mode,c.awb_gains))
    print('brightness {}  contrast {}'.format(c.brightness,c.contrast))
    print('dynamic range compression {}'.format(c.drc_strength))
    print('exposure compensation {}'.format(c.exposure_compensation))
    print('exposure mode {}'.format(c.exposure_mode))
    print('exposure speed, shutter speed {} , {}  [microsec]'.format(c.exposure_speed,c.shutter_speed))
    print('image denoise {}'.format(c.image_denoise))
    print('image effect {}'.format(c.image_effect))
    print('ISO {}'.format(c.iso))
    print('exposure metering mode {}'.format(c.meter_mode))
    print('rotation angle {}'.format(c.rotation))
    print('saturation {}'.format(c.saturation))
    print('sharpness {}'.format(c.sharpness))
