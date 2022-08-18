T = int(input())
N = list(map(int, input().split()))
for n in N:
    Y = [i for i in range(1, n) if n % i == 0]
    if n == sum(Y):
        print("Perfect")
    elif n > sum(Y):
        print("Deficient")
    else:
        print("Abundant")