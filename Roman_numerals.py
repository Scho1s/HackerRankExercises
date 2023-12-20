import re

regex_pattern = re.compile(r'^M{,3}D{,3}C{,3}L{,3}X{,3}V{,3}I{,3}$')
print(str(bool(re.match(regex_pattern, input()))))
