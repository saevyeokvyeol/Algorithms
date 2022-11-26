def solution(n):
    lst = sorted(list(str(n)))
    lst.reverse()
    answer = ""

    for i in lst:
        answer += i

    return int(answer)

