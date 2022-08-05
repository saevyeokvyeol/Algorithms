N, K = map(int, input().split())
result = 0
for i in range(1, N + 1):
    if N % i == 0:
        result += 1
        if K == result:
            print(i)
            exit()
print(0)