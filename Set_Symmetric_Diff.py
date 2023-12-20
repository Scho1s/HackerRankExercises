if __name__ == "__main__":
    num_of_eng_studs = int(input())
    eng_studs = set(input().split())
    num_of_fr_studs = int(input())
    fr_studs = set(input().split())
    print(len(eng_studs.symmetric_difference(fr_studs)))