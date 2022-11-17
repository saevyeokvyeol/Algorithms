def solution(array):
    answer = [str(i).count('7') for i in array]
    return sum(answer)