# 첫 번째 풀이
now_time = list(map(int, input().split(':')))
start_time = list(map(int, input().split(':')))
remain_time = []
for n, s in zip(now_time, start_time):
    remain_time.append(s - n)
for i in range(2, 0, -1):
    if remain_time[i] < 0:
        remain_time[i] += 60
        remain_time[i - 1] -= 1
if remain_time[0] < 0:
    remain_time[0] += 24
print(str(remain_time[0]).zfill(2) + ":" + str(remain_time[1]).zfill(2) + ":" + str(remain_time[2]).zfill(2))

# 두 번째 풀이
h, m, s = map(int, input().split(':'))
now_time = h * 60 * 60 + m * 60 + s
h, m, s = map(int, input().split(':'))
start_time = h * 60 * 60 + m * 60 + s
remain_time = (start_time - now_time) % 86400
h = remain_time // (60 * 60)
m = remain_time % (60 * 60) // 60
s = remain_time % 60
print(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2), sep=":")