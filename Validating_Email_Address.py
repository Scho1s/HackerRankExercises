import re

def fun(s):
    pattern = '^[a-zA-Z0-9\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.search(pattern, s) is not None

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = 5
    emails = ["its@gmail.com1",
              "mike13445@yahoomail9.server",
              "rase23@ha_ch.com",
              "daniyal@gmail.coma",
              "thatisit@thatisit",
              ]
    for email in emails:
        print(fun(email))
    # n = int(input())
    # emails = []
    # for _ in range(n):
    #     emails.append(input())