if __name__ == "__main__":
    a_size = int(input())
    a_set = set(input().split(" "))
    b_size = int(input())
    b_set = set(input().split(" "))
    diff = [int(_) for _ in list(a_set.difference(b_set)) + list(b_set.difference(a_set))]
    diff.sort()
    for _ in diff:
        print(_)
