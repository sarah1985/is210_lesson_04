#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Looping Mathematical Calculations"""

import data

print data.TRANSACTIONS
TRANSACTIONS = data.TRANSACTIONS

NEW_LIST = [sum(amt) for amt in TRANSACTIONS]
print NEW_LIST

TOTAL = 0
MINIMUM = 1000000000
MAXIMUM = 0
for num in NEW_LIST:

    if num < MINIMUM:
        MINIMUM = num

    if num > MAXIMUM:
        MAXIMUM = num

    TOTAL += num
print '''
Minimum Daily Transaction Total: {}
Maximum Daily Transaction Total: {}
Total Transaction Total: {}'''.format(MINIMUM, MAXIMUM, TOTAL)


