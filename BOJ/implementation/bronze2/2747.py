# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    f1, f2, f3 = 0, 1, 1
    for i in range(3, n + 1):
        f1, f2, f3 = f2, f3, f2 + f3
    return f3
    
n = int(input())
print(fibonacci(n))