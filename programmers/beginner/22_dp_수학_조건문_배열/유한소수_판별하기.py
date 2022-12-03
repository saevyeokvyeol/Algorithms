import math
def solution(a, b):
    bunmo = b // math.gcd(a, b)
    while bunmo % 2 == 0: bunmo //= 2
    while bunmo % 5 == 0: bunmo //= 5
    if bunmo == 1:
        return 1
    return 2