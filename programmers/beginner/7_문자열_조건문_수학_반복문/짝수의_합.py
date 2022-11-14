def solution(n, k):
    yang = 12000
    drink = 2000
    k -= n // 10
    answer = n * yang + k * drink
    return answer