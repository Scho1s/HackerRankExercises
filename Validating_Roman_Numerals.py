import re

regex_pattern = r'^M{0,3}(D?[C]{0,3}|C[DM])(L?[X]{0,3}|X[LC])(V?[I]{0,3}|I[VX])$'
print(str(bool(re.match(regex_pattern, input()))))
