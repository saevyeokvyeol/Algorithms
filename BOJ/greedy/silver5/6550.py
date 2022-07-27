while True:
    try:
        s, t = input().split()
        result = 'No'
        cnt = 0
        for i in t:
            if i == s[cnt]:
                cnt += 1
                if cnt == len(s):
                    result = 'Yes'
                    break
        print(result)
    except:
        break