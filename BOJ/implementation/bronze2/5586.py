string = input()
j = 0
i = 0
for s in range(len(string) - 2):
    if string[s:s + 3] == "JOI":
        j += 1
    elif string[s:s + 3] == "IOI":
        i += 1
print(j, i, sep="\n")