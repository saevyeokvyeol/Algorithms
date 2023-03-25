dish = input()
h = 10
for i in range(len(dish) - 1):
    if dish[i] == dish[i + 1]:
        h += 5
    else:
        h += 10
print(h)