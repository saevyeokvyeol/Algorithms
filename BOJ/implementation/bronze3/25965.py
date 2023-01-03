for _ in range(int(input())):
    n = int(input())
    donation = []
    for _ in range(n):
        donation.append(list(map(int, input().split())))
    k, d, a = map(int, input().split())
    print(sum([k * i - d * j + a * l for i, j, l in donation if k * i - d * j + a * l > 0]))