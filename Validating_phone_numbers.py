import re

pattern = r'^[7-9]{1}[0-9]{9}$'
numbers = [input() for _ in range(int(input()))]
for _ in numbers:
    if re.match(pattern, _):
        print("YES")
    else:
        print("NO")