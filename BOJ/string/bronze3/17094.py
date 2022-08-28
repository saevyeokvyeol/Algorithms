n = input()
s = input()
e = s.count('e')
two = s.count('2')
if e > two:
    print("e")
elif e < two:
    print("2")
else:
    print("yee")