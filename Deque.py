from collections import deque

d = deque()
current_value = None

deque_funcs = {'append': d.append,
               'appendleft': d.appendleft,
               'pop': d.pop,
               'popleft': d.popleft,
               }

if __name__ == "__main__":
    num_of_turns = int(input())
    for _ in range(num_of_turns):
        task = input()
        if len(task.split(" ")) > 1:
            method, current_value = task.split(" ")
            deque_funcs[method](int(current_value))
        else:
            method, current_value = task, None
            deque_funcs[method]()
    print(*d)
