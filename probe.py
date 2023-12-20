from time import time


def fact(n):
    if n in (0, 1):
        return 1
    return fact(n-1) * n


def fibo(n):
    result = [0, 1]
    if n <= 2:
        return result[:n]
    for _ in range(n - 2):
        result.append(sum(result[-2:]))
    return result


start = time()
a = fibo(500)
print(a)
print(f"Time lapsed: {time() - start} seconds")
