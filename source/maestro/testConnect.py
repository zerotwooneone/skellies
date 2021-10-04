import maestro
import time

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

#targets = [1,2000,3000,4000,6000,8000,9000]
#for channelIndex in [0,1]: #range(18):
#	print(f'channelIndex:{channelIndex}')
#	for target in targets:

#servo.setSpeed(channelIndex,60)
#servo.setAccel(channelIndex,100)
#servo.setTarget(channelIndex,target)

time.sleep(5)
servo.close
