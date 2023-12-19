N, X = map(int, input().split())
marks = []
for _ in range(X):
    marks.append(list(map(float, input().split())))
for _ in zip(*marks):
    print(sum(_)/len(_))
