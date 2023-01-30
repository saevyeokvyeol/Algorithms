P = ['apa', 'epe', 'ipi', 'opo', 'upu']
A = ['a', 'e', 'i', 'o', 'u']

string = input()
for p, a in zip(P, A):
    string = string.replace(p, a)
    
print(string)