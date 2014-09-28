#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Prompting inside a Loop Part I"""

VALID = False
INPUT_NUM = 0
FACTORIAL = 1
PRODUCT = 1

while not VALID:
    INPUT_NUM = int(raw_input('Input a number:'))

    if INPUT_NUM < 0:
        print 'Invalid number: Please enter a number greater than 0'

    else:
        break

while FACTORIAL <= INPUT_NUM:

    if INPUT_NUM > 1:
        PRODUCT *= FACTORIAL * INPUT_NUM * (INPUT_NUM - 1)

    else:
        PRODUCT = 1

OUTPUT = '''
Input value: {}
Factorial product: {}'''.format(INPUT_NUM, PRODUCT)

print OUTPUT
