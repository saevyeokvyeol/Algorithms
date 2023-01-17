string1 = input()
string2 = input()
minus = 0

for i in range(ord("a"), ord("z") + 1):
    a = chr(i)
    minus += max(string1.count(a), string2.count(a)) - min(string1.count(a), string2.count(a))
    
print(minus)