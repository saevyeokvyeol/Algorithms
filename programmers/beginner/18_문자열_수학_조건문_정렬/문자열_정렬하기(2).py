def solution(my_string):
    answer = sorted([i.lower() for i in my_string])
    return ''.join(answer)