def solution(array):
    result = []
    for i in set(array):
        result.append([i, array.count(i)])
    result.sort(key=lambda x:-x[1])
    answer = result[0][0] if len(result) == 1 or result[0][1] != result[1][1] else -1
    return answer