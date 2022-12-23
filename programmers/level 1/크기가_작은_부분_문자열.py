def solution(t, p):
    length = len(p)
    answer = 0
    for i in range(len(t) - length):
        if int(t[i:i + length]) <= int(p):
            answer += 1
    return answer