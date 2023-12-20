import re
from email.utils import parseaddr, formataddr
pattern = r'^[a-zA-Z]{1}[a-zA-Z0-9_.\-]{1,}[@]{1}[a-zA-Z]{1,}[.]{1}[a-zA-Z]{,3}$'
emails = [parseaddr(input()) for _ in range(int(input()))]
for _ in emails:
    if re.match(pattern, _[1]):
        print(formataddr(_))

"""
4
this <is@valid.com>
this <is_som@radom.stuff>
this <is_it@valid.com>
this <_is@notvalid.com>"""

