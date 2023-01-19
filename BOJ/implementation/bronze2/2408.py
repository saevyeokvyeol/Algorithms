n = int(input())
sic = ""
for _ in range(n * 2 - 1):
    sic += input()
sic = sic.replace("/", "//")
print(eval(sic))