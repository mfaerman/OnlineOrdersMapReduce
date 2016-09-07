#!/usr/bin/env python 

## Simulates streams of web page visits and purchase orders 

import random

NUM_CUSTOMERS = 200
NUM_WEB_PAGES = 100
NON_EVENT_PROBABILITY = 0.2
ORDER_PROBABILITY = 0.05
TIME_LIMIT = 100000

def generate_order(cid, ts, separator):
    print "c%d%s https://order?c%d.%d.html%s %d" %(cid, separator, cid, ts, separator, ts)

def generate_url(cid, ts, separator):
    web_page = random.randrange(NUM_WEB_PAGES)
    print "c%d%s http://Page%d.html%s %d" %(cid, separator, web_page, separator, ts)


def main(separator=','):

    customer_ids = range(20)

    random.seed(1)

    for ts in range(TIME_LIMIT):
        rand = random.random()
        cid = random.randrange(NUM_CUSTOMERS)


        if rand < NON_EVENT_PROBABILITY:
            # "Do nothing"
            pass
        elif rand <= NON_EVENT_PROBABILITY + ORDER_PROBABILITY:
            generate_order(cid, ts, separator)
        else:
            generate_url(cid, ts, separator)
              
if __name__ == "__main__":
    main()
