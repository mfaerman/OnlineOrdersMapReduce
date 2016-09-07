#!/usr/bin/env python  

import random

NUM_CUSTOMERS = 200
NUM_WEB_PAGES = 100
NON_EVENT_PROBABILITY = 0.2
ORDER_PROBABILITY = 0.05
TIME_LIMIT = 100000

separator = ','

customer_ids = range(20)

random.seed(1)

def generate_order(cid, ts):
    print "c%d%s https://order?c%d.%d.html%s %d" %(cid, separator, cid, ts, separator, ts)

def generate_url(cid, ts):
    web_page = random.randrange(NUM_WEB_PAGES)
    print "c%d%s http://Page%d.html%s %d" %(cid, separator, web_page, separator, ts)

ts = 0

for n in range(TIME_LIMIT):
    rand = random.random()
    cid = random.randrange(NUM_CUSTOMERS)


    if rand < NON_EVENT_PROBABILITY:
        # "Do nothing"
        pass
    elif rand <= NON_EVENT_PROBABILITY + ORDER_PROBABILITY:
        generate_order(cid, ts)
    else:
        generate_url(cid, ts)

    ts += 1
    
