import re

regex_integer_in_range = r'^[1-9]{1}\d{5}$'
regex_alternating_repetitive_digit_pair = r'^[1-9]{1}\$'

lst = ['012345',        # No
       '1234567',       # No
       '12345',         # No
       '123456',        # Yes
       '999999',        # Yes
       '123444',        # No
       '100000',        # No
       '121426',        # Yes
       '523563',        # Yes
       '552523',        # No
       ]
for _ in lst:
    result = re.findall(regex_integer_in_range, _)
    result2 = re.findall(regex_alternating_repetitive_digit_pair, _)
    # if result:
    #     print(result, end=', ')
    print(result2, end=', ')