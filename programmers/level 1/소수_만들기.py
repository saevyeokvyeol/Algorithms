from itertools import combinations

def solution(nums):
    num = [sum(n) for n in combinations(nums, 3)]
    answer = 0
    for n in num:
        if get_sosu(n):
            answer += 1
    return answer

def get_sosu(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True