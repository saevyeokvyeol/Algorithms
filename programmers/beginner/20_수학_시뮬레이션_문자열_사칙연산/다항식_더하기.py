def solution(polynomial):
    sic = polynomial.split(" + ")
    answer = [0] * 2
    for s in sic:
        if s.isdigit():
            answer[1] += int(s)
        else:
            answer[0] += 1 if len(s) == 1 else int(s.replace("x", ""))
    result = ''
    if answer[0] == 1:
        result += 'x'
    elif answer[0] > 1:
        result += str(answer[0]) + 'x'
    if len(result) > 0 and answer[1] != 0:
        result += ' + ' + str(answer[1])
    elif len(result) == 0:
        result += str(answer[1])
    return result