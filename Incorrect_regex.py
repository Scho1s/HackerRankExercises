""" This code doesn't work with Python 3, only PyPy """
import re

res = [input() for _ in range(int(input()))]
for _ in res:
    try:
        print(bool(re.compile(_)))
    except re.error:
        print(False)