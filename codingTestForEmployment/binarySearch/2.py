# 내 풀이: 브루트 포스
# n, m = map(int, input().split())
# dduk = list(map(int, input().split()))
# result = max(dduk) - 1

# while True:
#     get = 0
#     for d in dduk:
#         get += max(d - result, 0)
#     if get >= m:
#         print(result)
#         break
#     else:
#         result -= 1
        
# 내 풀이: 이진 탐색
n, m = map(int, input().split())
dduk = list(map(int, input().split()))
dduk.sort(reverse=True)
mid = max(dduk)

while True:
    get = 0
    for d in dduk:
        if d > mid:
            get += max(d - mid, 0)
        else:
            break
    if get == m:
        print(mid)
        break
    elif get > m:
        if mid // 2 == 0:
            print(mid + 1)
            break
        else:
            mid += mid // 2
    else:
        if mid // 2 == 0:
            print(mid)
            break
        else:
            mid -= mid // 2
            
# 예시 코드
# 떡의 개수(N)와 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 떄가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)