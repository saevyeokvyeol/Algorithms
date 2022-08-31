# 풀이 1
N, M, K = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)
result = 0
flag = 0
for i in range(M):
    if flag < K:
        result += num[0]
        flag += 1
    else:
        result += num[1]
        flag = 0
print(result)

# 풀이 2
N, M, K = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)
result = num[0] * (M - (M // (K + 1))) + num[1] * (M // (K + 1))
print(result)

# 예제
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
secont = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * K
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * secont # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력