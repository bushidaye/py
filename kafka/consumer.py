from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(group_id='123', bootstrap_servers='192.168.20.100:9092')
consumer.assign([TopicPartition(topic='topic3', partition=0)])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print recv
