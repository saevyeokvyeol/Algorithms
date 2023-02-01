cup = [0, 1, 0, 0]
order = input()
for o in order:
    if o == 'A':
        cup[1], cup[2] = cup[2], cup[1]
    elif o == 'B':
        cup[2], cup[3] = cup[3], cup[2]
    elif o == 'C':
        cup[1], cup[3] = cup[3], cup[1]
print(cup.index(1))