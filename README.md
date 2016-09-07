# OnlineOrdersMapReduce
Map-Reduce analysis for online purchase orders.

Derives which and how frequent web pages are visited immediately before customer issues purchase order

The computation consists of two Map-Reduce phases:

input -> order_mapper.py -> order_reducer.py -> WordCountMapper -> WordCountReducer

The input is assumed to be formatted as a list of comma separated (csv) triples: <customer id, url, time stamp>, one triple per line.

The code order_mapper.py emits a list of 4 element tuples: <customerd id, url, time stamp, url-type>
   url-type indicated if url is an online purchase order ('o'), or a regular url ('u').
   
The Map-Reduce framework, such as Hadoop, partitions order_mapper output by customer id. Each partition sent to reducers is sorted first by customer id and then by time stamp.

The reducers order_reducer.py emit list of urls of pages visited immediately preceeding purchase order.

The produced list of urls is fed into a regular WordCount Map-Reducer, such as this: 
