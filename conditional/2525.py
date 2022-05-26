import sys

# 1. 현재 시각을 저장한다
time = list(map(int, sys.stdin.readline().split()))

# 2. 요리 시간을 저장한다.
cook_time = int(input())

# 3. if문을 사용해 24시간 형태로 현재 시각에 요리 시간을 더한다.
time[1] += cook_time

while(time[1] >= 60):
  if time[1] >= 60 :
    time[1] -= 60
    time[0] += 1
    if time[0] >= 24:
      time[0] -= 24

# 4. 결과를 출력한다.
print(f'{time[0]} {time[1]}')