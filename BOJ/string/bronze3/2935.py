# 풀이 1
A = int(input())
O = input()
B = int(input())
if O == "+":
    print(A + B)
else:
    print(A * B)

# 풀이 2
A = input()
O = input()
B = input()
print(eval(A + O + B))