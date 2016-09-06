#!/usr/bin/env python                                                                                                                                        
"""Assumptions:
      - Input are files, each containing list of lines with the format -
         'customer-Id, URL, Time Stamp' """

from sys import stdin
import random

def is_order(string):
    if random.random() > 0.5:
        return 1
    else:
        return 0

def read_input(myfile):
    for line in myfile:
        yield line.split(',')

def main(separator='\t'):
    # input comes from STDIN (standard input)                                                                                                                
    data = read_input(stdin)

    for items in data:
        cid = items[0].strip()
        url = items[1].strip()
        ts = items[2].strip()
    
    # write the results to STDOUT (standard output);                                                                                                     
    # what we output here will be the input for the                                                                                                      
    # Reduce step, i.e. the input for reducer.py                                                                                                         
    #                                                                                                                                                    
    # tab-delimited; the trivial word count is 1                                                                                                         
        if is_order(url):
            print '%s%s%s%s%s%so' % (cid, separator, ts.zfill(8), separator, url, separator)
        else:
            print '%s%s%s%s%s%su' % (cid, separator, ts.zfill(8), separator, url, separator)

if __name__ == "__main__":
    main()

