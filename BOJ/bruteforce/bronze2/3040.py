N = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i + 1, 9):
        if sum(N) - N[i] - N[j] == 100:
            N.remove(N[j])
            N.remove(N[i])
            print(*N, sep="\n")
            exit()