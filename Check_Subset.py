A = set(map(int, input().split()))
subsets = []
for _ in range(int(input())):
    subsets.append(set(map(int, input().split())))
print(all([A.issuperset(_) for _ in subsets]))
