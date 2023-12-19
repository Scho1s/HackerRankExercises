import re

T = int(input())
lst = []
for _ in range(T):
    lst.append(input())

for uid in lst:
    if all([len(set(uid)) == len(uid),
            len(uid) == 10,
            re.search(r"^[a-zA-Z0-9]$", uid) is None,
            len(re.findall(r"[A-Z]", uid)) >= 2,
            len(re.findall(r"[0-9]", uid)) >= 3]):
        print("Valid")
    else:
        print("Invalid")
