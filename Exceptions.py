if __name__ == '__main__':
    test_cases = int(input())
    counter = 0
    results = []
    for _ in range(1, test_cases + 1):
        a, b = input().split(" ")
        try:
            results.append(int(int(a) / int(b)))
        except ZeroDivisionError as e:
            results.append(f"Error Code: integer division or modulo by zero")
        except ValueError as e:
            results.append(f"Error Code: {e}")
    for _ in results:
        print(_)
