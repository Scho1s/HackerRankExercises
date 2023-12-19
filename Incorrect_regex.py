import re

T = int(input())
for _ in range(T):
    try:
        re.search(input(), "qwertyuiop[]asdfghjkl;'#zxcvbnm,./+=_-")
        print(True)
    except re.error:
        print(False)