word = input().split()
ignore = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
print("".join([word[i][0].upper() for i in range(len(word)) if word[i] not in ignore or i == 0]))