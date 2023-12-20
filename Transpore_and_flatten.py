import numpy

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
arr = numpy.array(lst)
print(arr.transpose())
print(arr.flatten())