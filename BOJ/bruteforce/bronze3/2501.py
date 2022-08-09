# 풀이 1
N, K = map(int, input().split())
result = 0
for i in range(1, N + 1):
    if N % i == 0:
        result += 1
        if K == result:
            print(i)
            exit()
print(0)

# 풀이 2
N, K = map(int, input().split())
yaksu = [i for i in range(1, N + 1) if N % i == 0]
if len(yaksu) >= K:
    print(yaksu[K - 1])
else:
    print(0)