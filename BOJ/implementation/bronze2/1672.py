dna = [['A', 'C', 'A', 'G'], ['C', 'G', 'T', 'A'], ['A', 'T', 'C', 'G'], ['G', 'A', 'G', 'T']]
a = {'A':0, 'G':1, 'C':2, 'T':3}

n = int(input())
s = input()
end = s[-1]
for i in s[::-1][1:]:
    end = dna[a[i]][a[end]]
print(end)