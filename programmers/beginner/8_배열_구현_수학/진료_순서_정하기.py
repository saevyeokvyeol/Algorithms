# 첫 번째 풀이
def solution(emergency):
    answer = emergency
    order = sorted(emergency, reverse=True)
    i = 1
    for o in order:
        answer[emergency.index(o)] = i
        i += 1
    return answer

# 두 번째 풀이
def solution(emergency):
    answer = []
    i = 0
    while len(answer) != len(emergency):
        count = 1
        for j in emergency:
            if emergency[i] < j:
                count += 1
        answer.append(count)
        i += 1
    return answer