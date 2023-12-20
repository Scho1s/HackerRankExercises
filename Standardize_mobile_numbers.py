def wrapper(f):
    def fun(l):
        numbers = []
        for _ in l:
            start = len(_) % 5
            numbers.append(f"+91 {_[start:start+5]} {_[start+5:]}")
        f(numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


