black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))

for i in range(len(black)):
    black[i] -= white[i]

print(*black)