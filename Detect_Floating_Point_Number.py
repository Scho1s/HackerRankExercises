import re

T = int(input())
values = []
for _ in range(T):
    values.append(_)

for value in values:
    print(re.search(r"^[+\-]{0,1}[0-9]{0,}\.[0-9]+$", str(value)) is not None)
