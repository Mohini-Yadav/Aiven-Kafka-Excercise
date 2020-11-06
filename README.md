# AIVEN KAFKA

## Task: 
    Send events to a Kafka topic (a producer) which will then be read by a Kafka consumer application that you've written. 
    The consumer application must then store the consumed data to an Aiven PostgreSQL database.
      
## Assumption: 
    Kafka and PostgreSQL services sre running. 
    To keep things simple, Database name has been hardcoded to 'defaultdb'

## Installing Packages in PyCharm:
    This example uses the kafka-python library to interact with Kafka both as a producer of messages and a consumer.
    ```bash
    pip install kafka-python
    pip install kafka
    pip install psycopg2
    ```
## Running the Code:

1. Login to Aiven client, create a Kafka service and wait for it to be in running state 
2. Download all the Keys from the overview tab
3. Create a Topic eg. 'test'  in this project
4. Create PsotgreSQL service 
5. Open PyCharm and save producer.py, consumer.py and main.py
6. Run main.py and enter your choice between producer and consumer application
7. When the producer application runs it would ask the user to enter the 
   host uri and the path to the certification files. After that it would publish messages 
   within the specified range in the for loop.
8. This output would be displayed on the terminal and one can go on the Aiven GUI
   and click on the Topic tab. Then go to fetch messages to see the broadcasts.
   
9. If the Consumer application is run ,then the user would be prompted to enter the PostgreSQL
   details such as host, port, username, password in addition to details that were asked during producer application.
10. A DB table by the name "messages"  would be created if not already present. 
11. Once this step is successful, the published messages will be read by the Kafka consumer
    and displayed on the terminal and simultaneously would be entered in the database table.        
   
