long_string = input().split("-")
short_string = ""
for ls in long_string:
    short_string += ls[0]
print(short_string)