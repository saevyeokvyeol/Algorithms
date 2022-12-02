def solution(lines):
    lines.sort()
    answer = [-1] * 200
    for l in lines:
        for i in range(l[0], l[1] + 1):
            if answer[i + 100] == -1:
                answer[i + 100] = 0
            elif answer[i + 100] == 0:
                answer[i + 100] = 1
    return answer.count(1)