#!/usr/bin/python

import random
import os

def aRoll(howMany):
    try:
        thisMany = int(howMany)
    except:
        return "That's not a number"
    ans = []
    for each in range(thisMany):
        ans.append(random.randint(1,6))
    return ans

def roller():
    os.system('clear')
    howMany = raw_input('How many dice would you like to roll?\n\n')
    while True:
        os.system('clear')
        print
        print aRoll(howMany)
        print '\n\n\n\n\n\n\n\n\n\n\n'
        howMany = raw_input('How many dice would you like to roll?\n(x) to quit\n\n')
        if howMany == 'x':
            os.system('clear')
            break
        else:
            pass
