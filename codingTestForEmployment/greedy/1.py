# 풀이 1
n = int(input())
print(n // 500 + n % 500 // 100 + n % 100 // 50 + n % 50 // 10)

# 풀이 2
n = int(input())
coin = [500, 100, 50, 10]
cnt = 0
for c in coin:
    cnt += n // c
    n %= c
print(cnt)

# 예제
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)