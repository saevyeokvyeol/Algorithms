n = int(input())
nums = list(map(int, input().split()))
line = []

for i, num in zip(range(n), nums):
    line.insert(len(line) - num, i + 1)

print(*line)