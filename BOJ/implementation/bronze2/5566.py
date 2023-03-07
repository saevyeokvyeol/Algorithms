N, M = map(int, input().split())
kan = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]
here = 1

for m in range(M):
    here += dice[m]
    if here >= N:
        print(m + 1)
        break
    here += kan[here - 1]
    if here >= N:
        print(m + 1)
        break