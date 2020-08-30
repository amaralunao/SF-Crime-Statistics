from kafka import KafkaConsumer
import json


class ConsumerServer(KafkaConsumer):
    def __init__(self, topic_name):
        self.consumer = KafkaConsumer(
            bootstrap_servers="localhost:9092",
            request_timeout_ms=1000,
            auto_offset_reset="earliest",
            max_poll_records=10
        )
        self.consumer.subscribe(topics=topic_name)

    def consume(self):
        while True:
            for metadata, consumer_record in self.consumer.poll().items():
                if consumer_record is not None:
                    for record in consumer_record:
                        print(json.loads(record.value))
                else:
                    print("no message")


if __name__ == "__main__":
    consumer = ConsumerServer("calls")
    consumer.consume()