#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py, reducer.y -mapper mapper.py -reducer reducer.py -input /user/cloudera/mapreduce/test assign ment.txt -output /user/cloudera/mapreduce/outputassignment