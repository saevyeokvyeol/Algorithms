n = int(input())
for i in range(n):
    input()
    c, y, S, s, f = map(int, input().split())
    b, G, g, w = map(int, input().split())
    fancake = min(c // 0.5, y // 0.5, S // 0.25, s // 0.0625, f // 0.5625)
    topping = b + G // 30 + g // 25 + w // 10
    print(int(min(fancake, topping)))