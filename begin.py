import picamera.array, cv2,numpy,time
with picamera.PiCamera() as camera:
    camera.led = False
    framerate = 90
    time.sleep(1)
    camera.awb_mode = "off"
    g = camera.awb_gains
    camera.awb_gains = g
    camera.framerate = framerate
    camera.shutter_speed = int(1000000/camera.framerate) #Shutter speed is in microseconds
    camera.exposure_mode = "off"
    camera.iso = 200
    time.sleep(1)
    with picamera.array.PiRGBArray(camera) as stream:
        while 1:
            camera.capture(stream, "rgb")
            img=stream.array
            #print(numpy.array(img).shape)
            print(numpy.max(img))
            stream.seek(0)
            stream.truncate()
    