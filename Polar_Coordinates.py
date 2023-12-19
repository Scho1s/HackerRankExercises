from cmath import phase

if __name__ == "__main__":
    z = input().replace("j", "").replace("-", " -").replace("+", " +").strip()
    x, y = map(int, z.split(" "))
    print(abs(complex(x, y)))
    print(phase(complex(x, y)))
