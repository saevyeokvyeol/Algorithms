def solution(absolutes, signs):
    answer = 0
    for n, flag in zip(absolutes, signs):
        if not flag:
            n *= -1
        answer += n
    return answer