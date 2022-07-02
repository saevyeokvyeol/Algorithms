n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

sosu = [True for _ in range(max(num) + 1)]
sosu[0], sosu[1] = False, False

for i in range(2, int(len(sosu) ** 0.5) + 1):
    if sosu[i] == True:
        for j in range(i * 2, len(sosu), i):
            sosu[j] = False

for i in num:
    x = i // 2
    while x >= 2:
        if sosu[x] == True and sosu[i - x] == True:
            print(x, i - x)
            break
        else:
            x -= 1