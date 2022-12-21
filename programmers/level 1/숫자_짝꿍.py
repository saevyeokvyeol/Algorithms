def solution(X, Y):
    answer = ''
    for i in range(10):
        s = str(i)
        answer += s * min(X.count(s), Y.count(s))
    if len(answer) > 0 and answer[-1] == '0':
        answer = '0'
    return answer[::-1] if len(answer) != 0 else '-1'