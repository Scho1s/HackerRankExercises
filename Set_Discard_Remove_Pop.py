
if __name__ == "__main__":
    num_of_els = int(input())
    elements = set(map(int, input().split()))
    num_of_commands = int(input())
    set_operations = {'pop': elements.pop,
                      'remove': elements.remove,
                      'discard': elements.discard,
                      }
    for _ in range(num_of_commands):
        command = input()
        if command == "pop":
            set_operations["pop"]()
        else:
            comm, value = command.split(" ")
            if (comm == "remove" and int(value) in elements) or comm == "discard":
                set_operations[comm](int(value))

    sum_ = sum([int(_) for _ in elements])
    print(sum_)
