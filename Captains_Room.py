from collections import Counter

if __name__ == "__main__":
    K = int(input())
    D = Counter(input().split())
    for key, value in D.items():
        if value != K:
            print(key)
