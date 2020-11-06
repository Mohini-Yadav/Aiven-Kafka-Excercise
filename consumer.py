# A Kafka client that consumes records from a Kafka Topic.
from kafka import KafkaConsumer
import psycopg2


def consumer_example(service_uri, ca_cert_file, access_key_file, access_cert_file, db_user, db_password, host, port):
    consumer = KafkaConsumer(
        bootstrap_servers=service_uri,
        auto_offset_reset='earliest',
        security_protocol="SSL",
        ssl_cafile=ca_cert_file,
        ssl_keyfile=access_key_file,
        ssl_certfile=access_cert_file,
        consumer_timeout_ms=1000,
        fetch_max_wait_ms=10000,
    )

    # Use the connect() method of psycopg2 with required arguments to connect PostgreSQL.
    connection = psycopg2.connect(user=db_user,
                                  password=db_password,
                                  host=host,
                                  port=port,
                                  database="defaultdb")

    # Create a cursor object using the connection object returned by the connect method to execute PostgreSQL queries
    # from Python.
    cursor = connection.cursor()

    # Prepare a create table query.
    create_table_query = '''CREATE TABLE IF NOT EXISTS messages
                  (
                  MESSAGE           VARCHAR(25)
                  ); '''

    # Execute the query using a cursor.execute()
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    consumer.subscribe(['test'])
    for message in consumer:
        # Prepare a insert into table query.
        postgres_insert_query = """ INSERT INTO messages VALUES (%s)"""
        record_to_insert = (message.value.decode('utf-8'))
        cursor.execute(postgres_insert_query, (record_to_insert,))
        print("Record inserted with {}".format(record_to_insert))

    # closing database connection, cursor & consumer.
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
    consumer.close()
