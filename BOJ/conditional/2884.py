import sys

# 시간을 입력받는다
time = list(map(int, sys.stdin.readline().split()))

# 입력받은 시간에서 45를 뺀다
time[1] -= 45

# 만약 분이 0보다 작을 경우
if time[1] < 0:
  
  # 시에서 1을 빼고 분에 60을 더해 시간을 맞춘다
  time[0] -= 1
  time[1] += 60

  # 만일 시가 0보다 작을 경우
  if time[0] < 0:

    # 23을 더해 24시간제 규칙에 맞춘다
    time[0] += 24

# 결과를 출력한다
print(time[0], time[1])