import sys

# while문을 이용한 풀이 *********************************
time = list(map(int, sys.stdin.readline().split()))

cook_time = int(sys.stdin.readline())

time[1] += cook_time

while time[1] >= 60:
  time[1] -= 60
  time[0] += 1
  if time[0] >= 24:
    time[0] -= 24

print(time[0], time[1])

# 시간을 계산하는 풀이 *********************************
time = list(map(int, sys.stdin.readline().split()))

cook_time = int(sys.stdin.readline())

time[0] += (time[1] + cook_time) // 60
time[1] = (time[1] + cook_time) % 60

if time[0] >= 24:
  time[0] -= 24

print(time[0], time[1])