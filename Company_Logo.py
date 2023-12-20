from collections import OrderedDict


if __name__ == "__main__":
    company_name = input()
    name_dict = OrderedDict()
    name_list = list(company_name)
    name_list.sort()
    for letter in name_list:
        if letter in name_dict.keys():
            name_dict[letter] += 1
        else:
            name_dict[letter] = 1
    top_3 = sorted(name_dict.items(), key=lambda x: x[1], reverse=True)[:3]
    for letter, count in top_3:
        print(letter, count)
