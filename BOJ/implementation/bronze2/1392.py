n, q = map(int, input().split())
akbo = [int(input()) for _ in range(n)]
for i in range(n - 1, -1, -1):
    akbo[i] += sum(akbo[:i])
for i in range(q):
    question = int(input())
    for j in range(n):
        if question < akbo[j]:
            print(j + 1)
            break