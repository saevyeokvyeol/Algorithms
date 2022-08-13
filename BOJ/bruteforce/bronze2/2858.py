# 풀이 1
R, B = map(int, input().split())
b = [i for i in range(1, B + 1) if B % i == 0]
for i in b:
    if (i * 2) + (B // i + 2) * 2 == R:
        L, W = R // 2 - i, i + 2
        print(max(L, W), min(L, W))
        break

# 풀이 2
R, B = map(int, input().split())
A = R + B
for i in range(1, R):
    if A % i != 0:
        continue
    if (i * 2) + (A // i * 2) - 4 == R:
        print(A // i, i)
        break