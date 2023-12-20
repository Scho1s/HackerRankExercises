import re
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
S = input()
result = re.findall(r'(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}[aeiouAEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}))', S)
if result:
    for _ in result:
        print(_[1:-1])
else:
    print(-1)