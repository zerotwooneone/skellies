import maestro
import time

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

channels = [0,1] #range(18)
targets = [3000,9000] #[1,2000,3000,4000,6000,8000,9000]
#speeds = [0,1,60]
accels = [0,1,100,255]
try:
	#for speed in speeds:
	for acc in accels:
		for target in targets:
			for channelIndex in channels:
				print(f'ch: {channelIndex} acc:{acc} tar:{target}')
				print(f'min:{servo.getMin(channelIndex)} max:{servo.getMax(channelIndex)} pos:{servo.getPosition(channelIndex)} isMov:{servo.isMoving(channelIndex)} gMov:{servo.getMovingState()}')
				#servo.setSpeed(channelIndex,speed)
				servo.setAccel(channelIndex,acc)
				servo.setTarget(channelIndex,target)
				time.sleep(5)
finally:
	print('closing connection')
	servo.close()
