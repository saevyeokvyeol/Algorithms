n = int(input())
nums = list(map(int, input().split()))
score = nums[0]

for i in range(1, n):
    if nums[i] != nums[i - 1] + 1:
        score += nums[i]

print(score)