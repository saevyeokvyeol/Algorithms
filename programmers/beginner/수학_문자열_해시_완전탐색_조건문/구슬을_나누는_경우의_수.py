def solution(balls, share):
    answer = factorial(balls) // (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    answer = 1
    for i in range(n):
        answer *= i + 1
    return answer