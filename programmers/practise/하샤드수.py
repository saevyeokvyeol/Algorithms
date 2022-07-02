def solution(x):
    n = list(map(int, list(str(x))))
    if x % sum(n) == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))