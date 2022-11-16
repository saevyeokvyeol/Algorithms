def solution(num, k):
    try:
        return list(map(int, str(num))).index(k) + 1
    except:
        return -1