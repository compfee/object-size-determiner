from time import sleep
from picamera import PiCamera
import ultrasonic_distance
import sys
import numpy as np
import cv2 as cv
import imutils
import math

camera = PiCamera()
camera.resolution = (1280,720)
camera.start_preview()
#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
t=0


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while (t<5):
            t+=1;
            dist = distance()
            #print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

sleep(2)
camera.capture('test_image.png')
camera.stop_preview()


hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

if __name__ == '__main__':
    fn = 'test_image.png'
    img = cv.imread(fn)


    hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
    thresh = cv.inRange( hsv, hsv_min, hsv_max )
    _, contours0, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
    	cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv.contourArea)
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    width=extRight[0]-extLeft[0]
    height=extBot[1]-extTop[1]

    index = 0
    layer = 0

    def update():
        vis = img.copy()
        cv.drawContours( vis, contours0, index, (255,0,0), 2, cv.LINE_AA, hierarchy, layer )
        cv.circle(vis, extLeft, 8, (0, 0, 255), -1)
        cv.circle(vis, extRight, 8, (0, 255, 0), -1)
        cv.circle(vis, extTop, 8, (255, 0, 0), -1)
        cv.circle(vis, extBot, 8, (255, 255, 0), -1)
        
        print(extLeft)
        print(extRight)
        print(extTop)
        print(extBot)
       
        
        #print('height in pixels: ' + height)
        #print(height)
       # print('width in pixels: ' + width)
       # print(width)
       
        object_height_pixels= height
        object_width_pixels=width
        distance_to_object = distance()

        #sensor_height_mm = 3.68
        #sensor_width_mm = 2.76

        sensor_height_mm = 2.4
        sensor_width_mm = 2.4
        sensor_height_pixels = 720
        sensor_width_pixels = 720
        focal_length_mm = 3.04


        object_height_on_sensor_mm = (float)((sensor_height_mm * object_height_pixels) / sensor_height_pixels)
        object_width_on_sensor_mm = (float)((sensor_width_mm * object_width_pixels) / sensor_width_pixels)
        real_object_height = (float)((distance_to_object * object_height_on_sensor_mm) / focal_length_mm)-1
        real_object_width = (float)((distance_to_object * object_width_on_sensor_mm) / focal_length_mm)-1
        print "real height:"
        print(real_object_height)
        print "real width:"
        print(real_object_width )
    
        
        cv.imshow('contours', vis)
    def update_index(v):
        global index
        index = v-1
        update()

    def update_layer(v):
        global layer
        layer = v
        update()

    update_index(0)
    update_layer(0)
    cv.createTrackbar( "contour", "contours", 0, 7, update_index )
    cv.createTrackbar( "layers", "contours", 0, 7, update_layer )

    cv.waitKey()
    cv.destroyAllWindows()