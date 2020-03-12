from confluent_kafka import Consumer, KafkaError

def main():
    KAFKA_BROKER_URL = 'localhost:9092'
    KAFKA_CONSUMER_SESSION_TIMEOUT = 10000
    KAFKA_QUEUED_MAX_MESSAGE_KB = 2000000

    subscribe_topics = ["test"]
    print('Starting consumer on topic ' + str(subscribe_topics))
    c = Consumer({'bootstrap.servers': KAFKA_BROKER_URL,'group.id': 'testgroup', 'security.protocol' : 'SASL_PLAINTEXT', 'sasl.username': 'admin', 'sasl.password': 'admin-secret', 'sasl.mechanism':'PLAIN',
                  'default.topic.config': {'auto.offset.reset': 'smallest'}, 'session.timeout.ms': KAFKA_CONSUMER_SESSION_TIMEOUT,
                  'queued.max.messages.kbytes': KAFKA_QUEUED_MAX_MESSAGE_KB})
    print("Subscribing to npsservice topic")
    c.subscribe(subscribe_topics)
    running = True

    print('Start job ......................................')


    try:
        while running:
            print('Job working')
            msg = c.poll()
            if not msg.error():
                print('Received message: %s' % msg.value().decode('utf-8'))
                print(msg.value().decode('utf-8'))

            elif msg.error().code() != KafkaError._PARTITION_EOF:
                print(msg.error())
                running = False
        c.close()
    except KeyboardInterrupt:
        c.close()
        pass

    return True

main()