import numpy

N, M, P = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N+M)]
arr = numpy.concatenate(tuple(lst)).reshape(N+M, P)
print(arr)
