#!/usr/bin/env python                                                                                                                                        
"""Assumptions:
      - Input are files, each containing list of lines with the format -
         'customer-Id, URL, Time Stamp'  """

PADDING_LENGTH = 8
INPUT_SEPARATOR = ','

from sys import stdin
import random

def is_order(string):
    header_off = string.split("://",1)[1]
    if  header_off.find("order", 0) == 0:
        return True
    else:
        return False

def read_input(myfile):
    for line in myfile:
        yield line.split(INPUT_SEPARATOR)

def main(separator='\t'):
    # input comes from STDIN (standard input)                                                                                                                
    data = read_input(stdin)

    for items in data:
        cid = items[0].strip()
        url = items[1].strip()
        ts = items[2].strip().zfill(PADDING_LENGTH)
    
    # write the results to STDOUT (standard output);                                                                                                     
        output = '%s%s%s%s%s%s' % (cid, separator, ts, separator, url, separator)
        
        if is_order(url):
            print output + 'o'
        else:
            print output + 'u'

if __name__ == "__main__":
    main()
