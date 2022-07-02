def solution(n):
    answer = n ** 0.5
    if answer == int(answer):
        return (answer + 1) ** 2
    else:
        return -1