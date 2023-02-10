for _ in range(int(input())):
    T = list(map(int, input().split(":")))
    T2 = [str(bin(t)[2:]).zfill(6) for t in T]

    for i in range(6):
        for t in T2:
            print(t[i], end="")
    print(end=" ")
    print(*T2, sep="")