#!/usr/bin/env python                                                                                                                                        
"""Assumptions:
      - Input are files, each containing list of lines with the format -
         'customer-Id, URL, Time Stamp' """

from sys import stdin
import random

def is_order(string):
    if random.random() > 0.5:
        return True
    else:
        return False

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

        output = '%s%s%s%s%s%s' % (cid, separator, ts.zfill(8), separator, url, separator)
        
        if is_order(url):
            print output + 'o'
        else:
            print output + 'u'

if __name__ == "__main__":
    main()

