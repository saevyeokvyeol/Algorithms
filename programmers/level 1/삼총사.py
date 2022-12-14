from itertools import combinations
def solution(number):
    three = list(combinations(number, 3))
    return sum([1 for t in three if sum(t) == 0])