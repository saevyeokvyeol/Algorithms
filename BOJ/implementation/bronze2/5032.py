e, f, c = map(int, input().split())
bottle = e + f
drink = 0
while bottle >= c:
    change = bottle // c
    bottle = bottle % c + change
    drink += change
print(drink)