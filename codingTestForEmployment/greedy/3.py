# 풀이 1
N, M = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(N)]
card.sort(key=lambda x:-min(x))
print(min(card[0]))

# 풀이 2
N, M = map(int, input().split())
min_card = 0
for i in range(N):
    card = list(map(int, input().split()))
    min_card = max(min_card, min(card))
print(min_card)

# min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

# 2중 반복문 구조를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력