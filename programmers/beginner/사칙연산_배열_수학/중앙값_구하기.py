def solution(array):
    array.sort()
    middle = len(array) // 2
    return array[middle]