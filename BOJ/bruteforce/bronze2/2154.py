# 풀이 1
M = "".join([str(i) for i in range(1, 100001)])
N = input()
print(M.index(N) + 1)

# 풀이 2
M = "".join([str(i) for i in range(1, 100001)])
N = input()
print(M.find(N) + 1)

# 풀이 3
M = "".join([str(i) for i in range(1, 100001)])
N = input()
for i in range(len(M)):
    if M[i:i + len(N)] == N:
        print(i + 1)
        break