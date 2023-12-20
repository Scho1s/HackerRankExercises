def minion_game(string):
    consonants = [_ for _ in range(len(string)) if string[_] not in ['A', 'E', 'I', 'O', 'U']]
    vowels = [_ for _ in range(len(string)) if string[_] in ['A', 'E', 'I', 'O', 'U']]
    conso_result = sum(len(string) - _ for _ in consonants)
    vowel_result = sum(len(string) - _ for _ in vowels)
    if conso_result > vowel_result:
        print(f"Stuart {conso_result}")
    elif vowel_result > conso_result:
        print(f"Kevin {vowel_result}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
