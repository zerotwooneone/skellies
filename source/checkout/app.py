from dapr.clients import DaprClient
import json
import time
import logging

logging.basicConfig(level=logging.INFO)

logging.info('started checkout')

with DaprClient() as client:
    for i in range(1, 10):
        order = {'orderId': i}
        # Publish an event/message using Dapr PubSub
        result = client.publish_event(
            pubsub_name='orderpubsub',
            topic_name='orders',
            data=json.dumps(order),
            data_content_type='application/json',
        )
        logging.info('Published data: ' + json.dumps(order))
        time.sleep(1)
        

    """
    testData = {'test': 1}
    logging.info('about to Publish testRange')
    # Publish an event/message using Dapr PubSub
    result = client.publish_event(
        pubsub_name='orderpubsub',
        topic_name='testRange',
        data=json.dumps(testData),
        data_content_type='application/json',
    )
    logging.info('Published testRange.')
    """

    logging.info('about start goTo test')
    channels = [0] #range(18)
    targets = [3000, 3500, 6500, 8000,9000] #[1,2000,3000,4000,6000,8000,9000]
    #speeds = [0,1,60]
    accels = [1] #,100,255
    #for speed in speeds:
    for acc in accels:
        for target in targets:
            testData = {'channelIndex': 0, 'accel':acc, 'target':target}
            logging.info('about to Publish goto: ' + json.dumps(testData))
            result = client.publish_event(
                pubsub_name='orderpubsub',
                topic_name='goTo',
                data=json.dumps(testData),
                data_content_type='application/json',
            )
            logging.info('Published goto: ' + json.dumps(testData))
            time.sleep(5)
            
