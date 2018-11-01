from kafka import KafkaConsumer

consumer = KafkaConsumer('topic1', bootstrap_servers='192.168.20.100:9092')

for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print recv
