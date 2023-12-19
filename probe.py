import re

pattern = r"[0-9]"
print(len(re.findall(pattern, "B1CD102354")))