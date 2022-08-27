n = int(input())
M = [input() for _ in range(n)]
state = int(input())
if state == 2:
    for i in range(n):
        M[i] = M[i][::-1]
elif state == 3:
    M.reverse()

print(*M, sep="\n")