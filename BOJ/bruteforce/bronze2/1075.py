# 풀이 1
N = input()
F = int(input())
for i in range(int(N[:-2] + '00'), int(N[:-2] + '99') + 1):
    if i % F == 0:
        print(str(i)[-2:])
        break

# 풀이 2
N = int(input()[:-2] + "00")
F = int(input())
while N % F != 0:
    N += 1
print(str(N)[-2:])