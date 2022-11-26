def solution(n, m):
    small = min(n, m)

    for i in range(small + 1, 1, -1):
        if n % i == 0 and m % i == 0:
            return [i, (n * m) // i]
    return [1, n * m]

print(solution(3, 12))
print(solution(13, 26))