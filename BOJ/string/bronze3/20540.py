# 풀이 1
# mbti = {'I':'E', 'E':'I', 'S':'N', 'N':'S', 'T':'F', 'F':'T', 'J':'P', 'P':'J'}
# ideal = ''
# for m in input():
#     ideal += mbti[m]
# print(ideal)

# 풀이 2
ideal = 'EISNTFJP'
for m in input():
    ideal = ideal.replace(m, '')
print(ideal)