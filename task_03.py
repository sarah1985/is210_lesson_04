#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Prompting inside a Loop Part II"""

import data
ACCESS = False
PASSWORD = 'None'
ATTEMPTS = 3

while not ACCESS:
    PASSWORD = raw_input('What is your password ({} attempts left.)?'.format(ATTEMPTS))
    ATTEMPTS = ATTEMPTS - 1

    if PASSWORD == data.PASSWORD and ATTEMPTS > 0:
        ACCESS = True
        print 'Access granted!'

    else:
        if ATTEMPTS < 1:
            ACCESS = False
            print 'Access is denied, please try again later.'
            break