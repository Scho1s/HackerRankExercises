#!/bin/python3

import math
import os
import random
import re
import sys

def missingCharacters(s):
    chars = list('0123456789abcdefghijklmnopqrstuvwxyz')
    for _ in s.lower():
        try:
            chars.remove(_)
        except:
            pass
    return "".join(chars)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = missingCharacters(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()