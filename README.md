# SF Crime Statistics with Spark Streaming Project

## Introduction 

The purpose of this project is to showcase Kafka and Spark Structured Streaming integration.
A Kafka Producer publishes data onto a topic and the data can be consumed with both a Kafka Consumer 
or streaming analytics can be computed, namely an hourly count of distinct crime types from a police crime datasource.

## Requirements

* Java 1.8.x
* Scala 2.11.x
* Spark 2.4.x
* Kafka
* Python 3.7 or above

## Running the project

1. Start Zookeeper server:

* `/usr/bin/zookeeper-server-start config/zookeeper.properties`

2. Start Kafka server:

* `/usr/bin/kafka-server-start config/server.properties`

3. Copy the `police-department-calls-for-service.json` in the same folder as `kafka_server.py`
*  (The file was too big to be included in the repository.)
   
4. Produce data onto the topic:

* `python kafka_server.py`

5. Data can be consumed with:

* `kafka-console-consumer --topic "calls" --from-beginning --bootstrap-server localhost:9092`
 or
* `python consumer_server.py`

6. Spark job can be run with:

* `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`

## Screenshots

### Console Output - Kafka Consumer

https://github.com/amaralunao/SF-Crime-Statistics/blob/master/screenshots/console_consumer_output.png

### Progress reporter

https://github.com/amaralunao/SF-Crime-Statistics/blob/master/screenshots/progress_report.png

### Spark Count Output

https://github.com/amaralunao/SF-Crime-Statistics/blob/master/screenshots/spark_count.png

## Questions

** Q1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
* It has an effect on processedRowsPerSecond, but since `maxOffsetsPerTrigger=200`, and considering data size the impact is limited.

** Q2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
We need to maximize processedRowsPerSecond. Taking into consideration the size of data, max partition size and number of processors/cores - it is best to tweak:
* `spark.default.parallelism` -> 4
* `spark.sql.shuffle.partitions` -> 12
* `spark.streaming.kafka.maxRatePerPartition` -> 10000 