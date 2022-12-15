def solution(num):
    answer = 0
    for n in range(2, num + 1):
        answer += getSosu(n)
    return answer

def getSosu(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1