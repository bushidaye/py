# _*_coding:utf-8_*_

import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.20.100:9092')
# 新版kafka不再使用zookeeper地址,本地host文件需要写kafka主机名
msg_dict = {
    "name": "liu meng",
    "age": 23,
    "love": "peng",
    "intersest": {
        "food": "guo ba",
        "drink": "beer"
    }
}
msg = json.dumps(msg_dict)
[producer.send("topic3", msg, partition=i) for i in range(9)]
producer.close()
