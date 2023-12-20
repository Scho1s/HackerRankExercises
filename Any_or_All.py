N, list_of_values = int(input()), list(map(int, input().split()))
print(all([x > 0 for x in list_of_values]) and any([x == x[::-1] for x in map(str, list_of_values)]))