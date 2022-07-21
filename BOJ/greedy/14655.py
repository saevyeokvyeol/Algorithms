N = int(input())
num1 = [abs(i) for i in map(int, input().split())]
num2 = [abs(i) * -1 for i in map(int, input().split())]
print(sum(num1) - sum(num2))