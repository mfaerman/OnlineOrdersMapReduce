#!/usr/bin/env python

## Reducer assumes partitions by customer id
## Each partition is sorted first by customer id (cid) and then by time stamp (ts)

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(myfile, separator='\t'):
    for line in myfile:
        yield line.rstrip().split(separator,1) 

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple url entries by customer id
    # and creates an iterator that returns consecutive keys and their group:
    #   current_cid - string containing the customer id (the key)
    #   group - iterator yielding all url entries  - [customer id, time stamp, url, url-type (order, no order)]   
    for current_cid, group in groupby(data, itemgetter(0)):
        predecessor_ts, predecessor_url = "0", "http://No.Predecessor.Order.html"

        for current_cid, values in group:
            ts, url, type = values.split(separator)
            if type == 'o':
                print predecessor_url # Emit URL for next MapReduce WordCount phase
            predecessor_ts, predecessor_url = ts, url

if __name__ == "__main__":
    main()
