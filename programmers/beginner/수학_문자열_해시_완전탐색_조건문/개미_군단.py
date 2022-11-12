def solution(hp):
    gaemi = [5, 3, 1]
    answer = 0
    for g in gaemi:
        answer += hp // g
        hp %= g
    return answer