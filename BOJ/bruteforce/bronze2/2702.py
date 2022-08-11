# 풀이 1
for _ in range(int(input())):
    n, m = map(int, input().split())
    yaksu = 1
    for i in range(2, min(n, m) + 1):
        while n % i == m % i == 0:
            n //= i
            m //= i
            yaksu *= i
    print(n * m * yaksu, yaksu)

# 풀이 2
import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(math.lcm(n, m), math.gcd(n, m))