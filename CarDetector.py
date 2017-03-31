import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "Clear",i
             GPIO.output(3, 0)  #Turn OFF LED
             os.system("vcgencmd display_power 0") #Turn off display
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "ALERT",i
             GPIO.output(3, 1)  #Turn ON LED
             os.system("vcgencmd display_power 1") #Turn on display
             #os.system("omxplayer alarm.mp3") #play alarm sound
             time.sleep(0.1)
