for _ in range(int(input())):
    first, second = input().split()
    lst = []
    for f, s in zip(first, second):
        n = ord(s) - ord(f)
        lst.append(n if n >= 0 else n + 26)
    print("Distances: ", end="")
    print(*lst)