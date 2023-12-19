import re


def replace_string(str_value):
    got_ors = re.search(r'(\s\|\|\s)', str_value)
    got_ands = re.search(r'(\s&&\s)', str_value)
    while got_ors or got_ands:
        str_value = (re.sub(r'(\s&&\s)', " and ", re.sub(f'(\s\|\|\s)', " or ", str_value)))
        got_ors = re.search(r'(\s\|\|\s)', str_value)
        got_ands = re.search(r'(\s&&\s)', str_value)
    return str_value


N = int(input())
strings = []
new_strings = []
for _ in range(N):
    strings.append(input())

for _ in strings:
    print(replace_string(_))
