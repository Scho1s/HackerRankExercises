if __name__ == "__main__":
    a_num = int(input())
    a_set = set(input().split())
    set_operations = {'intersection_update': a_set.intersection_update,
                      'update': a_set.update,
                      'symmetric_difference_update': a_set.symmetric_difference_update,
                      'difference_update': a_set.difference_update,
                      }
    other_sets = int(input())
    for _ in range(other_sets):
        command, set_num = input().split()
        b_set = set(input().split())
        set_operations[command](b_set)
    print(sum(map(int, a_set)))
