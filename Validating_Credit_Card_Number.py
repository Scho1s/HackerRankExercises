import re


def is_valid_number(value):
    new_value = value.replace("-", "")
    lst = value.split("-")
    lst_size = True
    if len(lst) == 4:
        lst_size = all([len(_) == 4 for _ in value.split("-")])
    if all([new_value.isdigit(),
            len(new_value) == 16,
            len(value) <= 19,
            re.search(r'(\d)\1{3}', new_value) is None,
            lst_size,
            value[0] in ('4', '5', '6')]):
        return True
    return False

list_of_values = ["7165863385679329",
                  "6175824393389297",
                  "5252248277877418",
                  "9563584181869815",
                  "5179123424576876",
                  ]

for _ in list_of_values:
    if is_valid_number(_):
        print(True)
    else:
        print(False)


# if __name__ == "__main__":
#     N = int(input())
#     for _ in range(N):
#         if is_valid_number(input()):
#             print("Valid")
#         else:
#             print("Invalid")
