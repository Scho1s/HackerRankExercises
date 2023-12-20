import numpy

size = list(map(int, input().split()))
arr1 = numpy.array([list(map(int, input().split())) for _ in range(size[0])], int)
arr2 = numpy.array([list(map(int, input().split())) for _ in range(size[0])], int)
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
print(arr1 ** arr2)