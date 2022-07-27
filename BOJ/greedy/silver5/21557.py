N = int(input())
flare = list(map(int, input().split()))
for _ in range(N - 3):
    if flare[0] > flare[-1]:
        flare[0] -= 1
    else:
        flare[-1] -= 1
print(max(flare[0], flare[-1]) - 1)