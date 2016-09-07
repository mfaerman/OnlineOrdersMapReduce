# OnlineOrdersMapReduce
##Map-Reduce analysis for online purchase orders.

Derives which and how frequent web pages are visited immediately before customer issues purchase order.

The computation consists of two Map-Reduce phases:

         input -> order_mapper.py -> order_reducer.py -> WordCountMapper -> WordCountReducer

The input is assumed to be formatted as a list of comma separated (csv) triples: 
         
         <customer id, url, time stamp>, one triple per line.

The code order_mapper.py emits a list of 4 element tuples: 

         <customerd id, url, time stamp, url-type>
   url-type indicated if url is an online purchase order ('o'), or a regular url ('u').
   
The Map-Reduce framework, such as Hadoop, partitions order_mapper output by customer id. Each partition sent to reducers is sorted first by customer id and then by time stamp.

The reducers order_reducer.py emit lists of urls of pages visited immediately before a purchase order is issued by a customer.

The produced list of urls is fed into a regular WordCount Map-Reducer, such as this nice Python example by Michael Noll: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/#mapperpy

Example hadoop commands (using Hadoop Streaming):
   - Order-Immediate-Predecessor-URL phase: 
   
         hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapred.reduce.tasks=12 -mapper ~/work/order_mapper.py -input input.txt -reducer ~/work/order_reducer.py -file ~/work/order_reducer.py -file ~/work/order_mapper.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf num.key.fields.for.partition=1 -jobconf stream.num.map.output.key.fields=2 -output omr-12-kpf2-emit-o

   - WordCount phase: 
   
         hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapred.reduce.tasks=2 -mapper ~/work/gmapper.py -input omr-12-kpf2-emit-o/* -reducer ~/work/greducer.py -file ~/work/greducer.py -file ~/work/gmapper.py -output wc1

Example of serial test using Unix pipes:

         ./generator.py | ./order_mapper.py | sort | ./order_reducer.py | ./gmapper.py | sort | ./greducer.py | sort -nk2 > output-test-check.txt


