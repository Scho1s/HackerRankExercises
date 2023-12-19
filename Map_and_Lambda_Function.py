cube = lambda x: x**3

def fibonacci(n):
    lst = [0, 1, 1]
    if n < 4:
        return lst[:n]
    for _ in range(n - 3):
        lst.append(sum(lst[-2:]))
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
