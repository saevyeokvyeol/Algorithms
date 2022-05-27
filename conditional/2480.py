import sys

# 내가 푼 문제
num = list(map(int, sys.stdin.readline().split()))
result = 0

if num[0] == num[1] and num[1] == num[2]:
  result = 10000 + num[0] * 1000
elif num[0] == num[1]:
  result = 1000 + num[0] * 100
elif num[0] == num[2]:
  result = 1000 + num[0] * 100
elif num[1] == num[2]:
  result = 1000 + num[1] * 100
else:
  result = max(num) * 100

print(result)

# 참고해 다시 푼 코드
num = sorted(list(map(int, sys.stdin.readline().split())))
# 리스트를 정렬하면 모든 숫자가 같지 않은 이상 첫 번째 숫자와 세 번째 숫자가 같을 수 없음
# 따라서 elif 단계가 하나 줄어든다
result = 0

if num[0] == num[1] == num[2]: # 세 수를 한꺼번에 비교할 수도 있다
  result = 10000 + num[0] * 1000
elif num[0] == num[1] or num[1] == num[2]:
  result = 1000 + num[1] * 100
else:
  result = max(num) * 100

print(result)


