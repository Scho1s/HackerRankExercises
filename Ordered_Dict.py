from collections import OrderedDict

ordered_dict = OrderedDict()


def extract_data(string):
    words = string.split(" ")
    price = words[-1]
    product = " ".join(words[:-1])
    return product, int(price)


if __name__ == "__main__":
    num_of_items = int(input())
    for str_value in range(num_of_items):
        new_item = input()
        product, price = extract_data(new_item)
        if product in ordered_dict.keys():
            ordered_dict[product] += price
        else:
            ordered_dict[product] = price

    for key, value in ordered_dict.items():
        print(key, value)
