n = 5
num = [int(input()) for _ in range(n)]
print(sum(num) // n)
print(sorted(num)[n // 2])