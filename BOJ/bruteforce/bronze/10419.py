# 풀이 1
for _ in range(int(input())):
    d = int(input())
    J = 0
    for i in range(d):
        if i ** 2 + i <= d:
            J = i
        else:
            break
    print(J)

# 풀이 2
for _ in range(int(input())):
    d = int(input())
    J = 0
    while (J + 1) ** 2 + (J + 1) <= d:
        J += 1
    print(J)