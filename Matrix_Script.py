import re

def join_lists(list_of_lists):
    result_ = []
    for list_ in list_of_lists:
        for letter in list_:
            result_.append(letter)
    return "".join(result_)


def decode(value):
    last_index = len(value) - 1
    first_index = 0
    while not value[first_index].isalnum() and first_index < len(value) - 1:
        first_index += 1
    first_index %= len(value) - 1
    while not value[last_index].isalnum() and last_index > 0:
        last_index -= 1

    new_value = value[:first_index] + re.sub(r'\W+', ' ', value[first_index:last_index]) + value[last_index:]
    print(new_value)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    matrix = []
    new_matrix = [[] for _ in range(m)]
    for row in range(n):
        for column in range(m):
            new_matrix[column].append(matrix[row][column])
    result = join_lists(new_matrix)
    decode(result)


"""
# i#
 @#U
Should result in #  @i U

# 
 @
Should result in #  @

"""
