def solution(my_string):
    answer = [int(s) for s in my_string if s.isdigit()]
    answer.sort()
    return answer