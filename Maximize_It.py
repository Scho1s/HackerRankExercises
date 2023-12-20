import random

if __name__ == "__main__":
    K, M = map(int, input().split())
    lists = [list(map(int, input().split()))[1:] for _ in range(K)]
    max_value = 0
    for _ in range(random.randint(0, 20000)):
        final_list = []
        for list_ in lists:
            final_list.append(list_[random.randint(0, len(list_) - 1)] ** 2)
        sum_of_elements = sum(final_list) % M
        if sum_of_elements > max_value:
            max_value = sum_of_elements
    print(max_value)
