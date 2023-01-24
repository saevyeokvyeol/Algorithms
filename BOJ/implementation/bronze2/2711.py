n = int(input())
for _ in range(n):
    num, string = input().split()
    num = int(num)
    ls = len(string)
    print(*[string[i] for i in range(ls) if i + 1 != num], sep="")