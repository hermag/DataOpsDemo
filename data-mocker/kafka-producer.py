#!/usr/bin/python
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='16.168.0.3,9092')

# Asynchronous by default
for i in range(1000):
    future = producer.send('test', b'RAW DATA %d'%i)
    # Block for 'synchronous' sends
    record_metadata = future.get(timeout=1)
    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)
    time.sleep(2)

