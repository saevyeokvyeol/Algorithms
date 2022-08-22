A, B, C, N = map(int, input().split())
for i in range(N // A + 1):
    for j in range(N // B + 1):
        if (N - (A * i) - (B * j)) % C == 0:
            print(1)
            exit()
        elif N - (A * i) - (B * j) < 0:
            break
print(0)