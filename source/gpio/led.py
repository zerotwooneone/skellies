import RPi.GPIO as GPIO
import time

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

while True:
	print "LED on"
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)


