from collections import OrderedDict

word_dict = OrderedDict()


if __name__ == "__main__":
    num_of_words = int(input())
    for _ in range(num_of_words):
        new_word = input()
        word_dict[new_word] = word_dict[new_word] + 1 if new_word in word_dict.keys() else 1
    print(len(word_dict))
    for _ in word_dict.values():
        print(_, end=' ')
