from confluent_kafka import Producer

KAFKA_PRODUCER_CONFIGURATION = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol' : 'SASL_PLAINTEXT',
    'sasl.username': 'admin',
    'sasl.password': 'admin-secret',
    'sasl.mechanism':'PLAIN'
    #'linger.ms': 0,
    #'compression.type': None,
    #'request.required.acks': 1,
    #'retries': 1,
    #'max.in.flight.requests.per.connection': 1
    }

producer = Producer(KAFKA_PRODUCER_CONFIGURATION)

# Write hello world to test topic
producer.produce("test", '{"name":"DGR"}')
producer.flush()