import sys
import math

# 테스트 케이스 수 받기
case = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for i in range(case):
  floor = int(sys.stdin.readline()) # 층 받기
  num = int(sys.stdin.readline()) # 호 받기
  result = [x for x in range(1, num + 1)] # 0층 거주자 리스트 생성
  print(result) # [1, 2, 3]

  for j in range(floor): # 입력받은 층까지 반복
    for k in range(1, num): # 입력받은 호까지 반복
      result[k] += result[k - 1] # 층/호가 올라가며 반복될 때마다 아래층 주민의 수 재계산
  
  print(result) # [1, 3, 6]
  print(result[-1]) # 마지막 원소 출력

# ####################################################################

# 재귀 함수

# 테스트 케이스 수 받기
case = int(sys.stdin.readline())

def result(k, n):
  if k == 0:
    return n
  people = 0
  for j in range(1, n+1):
    people += result(k-1, j)
  return people

for i in range(case):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  print(result(k, n))