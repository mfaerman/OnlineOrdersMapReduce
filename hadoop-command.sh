hadoop jar ../contrib/streaming/hadoop-0.20.1+169.89-streaming.jar -D mapred.reduce.tasks=4 -file ~/mayo/smplMapper.py -mapper smplMapper.py -file ~/mayo/smplReducer.py -reducer smplReducer.py -input customers.dat -input countries.dat -output mayo -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf stream.map.output.field.separator=^ -jobconf stream.num.map.output.key.fields=4 -jobconf map.output.key.field.separator=^ -jobconf num.key.fields.for.partition=1


hadoop jar ../contrib/streaming/hadoop-0.20.1+169.89-streaming.jar -D mapred.reduce.tasks=4 -file ~/mayo/smplMapper.py -mapper smplMapper.py -file ~/mayo/smplReducer.py -reducer smplReducer.py -input customers.dat -input countries.dat -output mayo -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf stream.map.output.field.separator=^ -jobconf stream.num.map.output.key.fields=4 -jobconf map.output.key.field.separator=^ -jobconf num.key.fields.for.partition=1

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapred.reduce.tasks=1 -file ~/work/order_mapper.py -mapper ~/work/order_mapper.py -input input.txt -output om1 -jobconf stream.num.map.output.key.fields=4 -D num.key.fields.for.partition=1


hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapreduce.job.reduces=2 -D mapreduce.partition.keypartitioner.options=3 -D =-k1,1 -file ~/work/order_mapper.py -file ~/work/order_reducer.py -mapper ~/work/order_mapper.py -input input.txt -reduc^C ~/work/order_reducer.py -output omr-4 


hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapred.reduce.tasks=10 -D stream.num.map.output.key.fields=3 -D mapred.text.key.partitioner.options=-k1 -D stream.map.output.field.separator=\t -D map.output.key.field.separator=\t -file ~/work/order_mapper.py -file ~/work/order_reducer.py -mapper ~/work/order_mapper.py -input input.txt -reducer ~/work/order_reducer.py -output omr-2k


hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapred.reduce.tasks=2 -file ~/work/order_mapper.py -mapper ~/work/order_mapper.py -input input.txt -reducer ~/work/order_reducer.py -file ~/work/order_reducer.py -output omr-2k

oop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -D mapred.reduce.tasks=10 -mapper ~/work/order_mapper.py -input input.txt -reducer ~/work/order_reducer.py -file ~/work/order_reducer.py -file ~/work/order_mapper.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf num.key.fields.for.partition=1 -jobconf stream.num.map.output.key.fields=2 -output omr-10-kpf