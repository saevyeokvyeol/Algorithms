def factorial(n):
    result = 1
    if n != 0:
        result = n
        result *= factorial(n - 1)
    return result

print(factorial(int(input())))