def solution(number, limit, power):
    sum = 0
    for i in range(1, number + 1):
        divisor = get_divisor_sum(i)
        sum += divisor if divisor <= limit else power
    return sum

def get_divisor_sum(n):
    divisor = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor += 2
    if int(n ** 0.5) == n ** 0.5:
        divisor -= 1
    return divisor