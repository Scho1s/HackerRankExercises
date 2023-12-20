import re

pattern = r'([a-zA-Z0-9]+)(\1)'
S = input()
matches = re.search(pattern, S)
if matches:
    print(S[matches.start()])
else:
    print(-1)