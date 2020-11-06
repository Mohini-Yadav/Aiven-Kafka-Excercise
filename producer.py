# This script connects to Kafka and send a few messages
from kafka import KafkaProducer


def producer_example(service_uri, ca_cert_file, access_key_file, access_cert_file):
    producer = KafkaProducer(
        bootstrap_servers=service_uri,
        security_protocol="SSL",
        ssl_cafile=ca_cert_file,
        ssl_keyfile=access_key_file,
        ssl_certfile=access_cert_file,
    )

    for i in range(150, 151):
        message = "msg{}".format(i)
        print("Sending: {}".format(message))
        producer.send("test", message.encode("utf-8"))

    # Wait for all messages to be sent
    producer.flush()
