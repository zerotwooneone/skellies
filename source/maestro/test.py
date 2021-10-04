import maestro
import time

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)
servo.setAccel(0,25)
servo.setTarget(0,6000)

servo.setAccel(0,50)
servo.setTarget(0,3000)

#servo.setAccel(1,25)
#servo.setTarget(1,6000)
time.sleep(2)
servo.setAccel(0,25)
servo.setTarget(0,1000)

servo.setAccel(0,200)
servo.setTarget(0,9000)


#servo.setAccel(1,25)
#servo.setAccel(1,1000)
servo.close
