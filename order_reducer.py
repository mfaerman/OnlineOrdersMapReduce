#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(myfile, separator='\t'):
    for line in myfile:
        yield line.rstrip().split(separator,1) 

# def find_predecessor(ots, group, separator='\t'):
#     for cid, values in group:
#         url, ts, type = values.split(separator)
#         if ts < ots:
#             pass

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_cid, group in groupby(data, itemgetter(0)):
#        print "-------------%s-------------" %current_cid
        predecessor_ts, predecessor_url = "0",""
#        try:
        for current_cid, values in group:
            ts, url, type = values.split(separator)
 #           print "%s --> %s '(%s)' t = %d" %(current_cid, url, type, int(ts))
            if type in 'o':
                print "%s%s1" %(predecessor_url, separator)
            predecessor_ts, predecessor_url = ts, url

#         except ValueError:
#             # count was not a number, so silently discard this item
#             pass

if __name__ == "__main__":
    main()
