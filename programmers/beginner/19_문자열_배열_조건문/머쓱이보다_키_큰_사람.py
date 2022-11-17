# 첫 번째 풀이
def solution(array, height):
    answer = len([i for i in array if i < height])
    return answer

# 두 번째 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)