import re

pattern = r'(?=([#]{1}[a-fA-F0-9]{3,6}[;,)]{1}))'

css = [input() for _ in range(int(input()))]
matches = re.findall(pattern, "".join(css))
for match in matches:
    print(match[:-1])
