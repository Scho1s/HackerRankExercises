import re

S, k = input(), input()

matches = [(_.start(), _.start() + len(k) - 1) for _ in re.finditer(r'(?=({}))'.format(k), S)]
if matches:
    for _ in matches:
        print(_)
else:
    print((-1, -1))

