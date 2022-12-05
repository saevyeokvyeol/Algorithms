# 첫 번째 풀이
def solution(before, after):
    alphabet = list(set(before))
    for a in alphabet:
        if before.count(a) != after.count(a):
            return 0
    return 1

# 두 번째 풀이
def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0