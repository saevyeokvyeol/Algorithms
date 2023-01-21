n = 10
num = [int(input()) for _ in range(n)]

often_num = None
count = 0
for i in set(num):
    if num.count(i) > count:
        often_num = i
        count = num.count(i)

print(sum(num) // n)
print(often_num)