#!/bin/bash
hdfs dfs -mv /ElephantGambit/raw_json/*json /ElephantGambit/for_compressing;
hive -f compress_to_avro.sql && hdfs dfs -rm /ElephantGambit/for_compressing/*


