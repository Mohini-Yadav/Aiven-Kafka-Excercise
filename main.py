import os
import sys
from Aiven_project.consumer import consumer_example
from Aiven_project.producer import producer_example


def main():
    # Ask for User's choice
    producer_consumer = input(
        "Please enter \"producer\" if you wish to run Producer application or \"consumer\" if you wish to run the "
        "Consumer application \n")
    application_type = producer_consumer.lower()
    if application_type == "producer":
        service_uri = input("Please enter Service URI in the form host:port \n")
        isblank_input(service_uri)
        ca_cert_file = input("Location of the CA certificate \n")
        validate_file(ca_cert_file)
        access_key_file = input("Location of the Kafka Access Key (obtained from Aiven Console) \n")
        validate_file(access_key_file)
        access_cert_file = input("Location of the Kafka Certificate Key (obtained from Aiven Console) \n")
        validate_file(access_cert_file)

        producer_example(service_uri, ca_cert_file, access_key_file, access_cert_file)

    elif application_type == "consumer":
        service_uri = input("Please enter Service URI in the form host:port \n")
        isblank_input(service_uri)
        ca_cert_file = input("Location of the CA certificate \n")
        validate_file(ca_cert_file)
        access_key_file = input("Location of the Kafka Access Key (obtained from Aiven Console) \n")
        validate_file(access_key_file)
        access_cert_file = input("Location of the Kafka Certificate Key (obtained from Aiven Console) \n")
        validate_file(access_cert_file)
        # DB credentials
        db_user = input("DB user name (obtained from Aiven Console) \n")
        db_password = input("DB password (obtained from Aiven Console) \n")
        host = input("localhost (obtained from Aiven Console) \n")
        port = input("post number (obtained from Aiven Console) \n")

        consumer_example(service_uri, ca_cert_file, access_key_file, access_cert_file, db_user, db_password, host, port)
    else:
        print("OOPS! Seems like you've entered a wrong choice. Please enter either producer or consumer")


# Function to check if the file exists on the path or not
def validate_file(file_name):
    if not os.path.isfile(file_name):
        print("File does not exist on the path. Please check and execute again!")
        sys.exit()


def isblank_input(answer):
    if answer == "":
        print("Sorry, Input cannot be blank!")
        exit()


if __name__ == '__main__':
    main()
