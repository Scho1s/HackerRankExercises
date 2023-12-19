from itertools import combinations

N, N_list, K = int(input()), input().replace(" ", ""), int(input())
print(len(list(_ for _ in combinations(N_list, K) if "a" in _))/len(list(_ for _ in combinations(N_list, K))))
