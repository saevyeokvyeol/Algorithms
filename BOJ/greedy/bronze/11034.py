# 풀이 1
while True:
    try:
        K = list(map(int, input().split()))
        count = 0
        while K[0] + 1 != K[1] or K[1] != K[2] - 1:
            left = K[1] - K[0]
            right = K[2] - K[1]
            if left > 1 or right > 1:
                if left > right:
                    K[1], K[2] = K[1] - 1, K[1]
                    count += 1
                else:
                    K[0], K[1] = K[1], K[1] + 1
                    count += 1
            else:
                break
        print(count)
    except:
        break

# 풀이 2
while True:
    try:
        K = list(map(int, input().split()))
        left = K[1] - K[0]
        right = K[2] - K[1]
        print(left - 1 if left > right else right - 1)
    except:
        break