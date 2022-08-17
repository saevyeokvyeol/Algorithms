while True:
    try:
        n = int(input())
        k = 1
        s = []
        while True:
            s.extend(list(str(n * k)))
            flag = True
            for i in range(10):
                if not str(i) in s:
                    flag = False
                    break
            if flag:
                print(k)
                break
            else:
                k += 1
    except:
        break