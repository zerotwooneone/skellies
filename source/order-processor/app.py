from flask import Flask, request, jsonify
from cloudevents.http import from_http
import json
import os
import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

logging.info('started order-processor')

app = Flask(__name__)

app_port = os.getenv('APP_PORT', '6002')

# Register Dapr pub/sub subscriptions
@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{
        'pubsubname': 'orderpubsub',
        'topic': 'orders',
        'route': 'orders'
    },
    {
        'pubsubname': 'orderpubsub',
        'topic': 'testRange',
        'route': 'testRange'
    },
    {
        'pubsubname': 'orderpubsub',
        'topic': 'goTO',
        'route': 'goTO'
    }]
    print('Dapr pub/sub is subscribed to: ' + json.dumps(subscriptions))
    return jsonify(subscriptions)


# Dapr subscription in /dapr/subscribe sets up this route
@app.route('/orders', methods=['POST'])
def orders_subscriber():
    event = from_http(request.headers, request.get_data())
    print('Subscriber received : %s' % event.data['orderId'], flush=True)
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}

@app.route('/testRange', methods=['POST'])
def testRange_subscriber():
    event = from_http(request.headers, request.get_data())
    
    logging.info('received testRange')
    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    channels = [0] #range(18)
    targets = [3000, 3500, 6500, 8000,9000,0] #[1,2000,3000,4000,6000,8000,9000]
    #speeds = [0,1,60]
    accels = [1] #,100,255
    try:
        #for speed in speeds:
        for acc in accels:
            for target in targets:
                for channelIndex in channels:
                    logging.info(f'ch: {channelIndex} acc:{acc} tar:{target}')
                    logging.info(f'min:{servo.getMin(channelIndex)} max:{servo.getMax(channelIndex)} pos:{servo.getPosition(channelIndex)} isMov:{servo.isMoving(channelIndex)} gMov:{servo.getMovingState()}')
                    #servo.setSpeed(channelIndex,speed)
                    servo.setAccel(channelIndex,acc)
                    servo.setTarget(channelIndex,target)
                    time.sleep(5)
    finally:
        logging.info('closing connection')
        servo.close()

@app.route('/goTO', methods=['POST'])
def goTo_subscriber():
    event = from_http(request.headers, request.get_data())
    
    logging.info('received goTO')
    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    try:
        channelIndex = event.data["channelIndex"]
        accel = event.data["accel"]
        target = event.data["target"]
        logging.info(f'about to goTo channelIndex: {channelIndex} accel:{accel} target:{target}')
        #logging.info(f'min:{servo.getMin(channelIndex)} max:{servo.getMax(channelIndex)} pos:{servo.getPosition(channelIndex)} isMov:{servo.isMoving(channelIndex)} gMov:{servo.getMovingState()}')
        #servo.setSpeed(channelIndex,speed)
        servo.setAccel(channelIndex,accel)
        servo.setTarget(channelIndex,target)
    finally:
        logging.info('closing connection')
        servo.close()
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}


app.run(port=app_port)

