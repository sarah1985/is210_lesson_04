#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: Analyze a String"""

import data
print data.SHAKESPEARE

SHAKESPEARE_LINES = data.SHAKESPEARE.split("\n")
ACC_MAX = 0
ACC_MIN = 100
ACC_TOTAL = 0
ACC_CRISPIAN = 0

for i in SHAKESPEARE_LINES:

    NUM_WORDS = len(i.split())

    if NUM_WORDS > ACC_MAX:
        ACC_MAX = NUM_WORDS

    if NUM_WORDS < ACC_MIN:
        ACC_MIN = NUM_WORDS

    if 'Crispian' in i:
        ACC_CRISPIAN = ACC_CRISPIAN + 1

    ACC_TOTAL = ACC_TOTAL + NUM_WORDS

print "ACC_MAX: {}".format(ACC_MAX)
print "ACC_MIN: {}".format(ACC_MIN)
print "ACC_CRISPIAN: {}".format(ACC_CRISPIAN)

MAXIMUM_WORDS = ACC_MAX
MINIMUM_WORDS = ACC_MIN
NUM_CRISPIAN = ACC_CRISPIAN
AVERAGE_WORDS = float(ACC_TOTAL)/len(SHAKESPEARE_LINES)
print "AVERAGE_WORDS: {}".format(AVERAGE_WORDS)