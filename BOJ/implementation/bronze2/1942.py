for _ in range(3):
    t1, t2 = map(int, input().replace(":", "").split())
    min_t = min(t1, t2)
    multiple_of_3 = 0

    for h in range(24):
        for m in range(60):
            for s in range(60):
                t = int(str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2))
                if min_t == t1:
                    if t1 <= t <= t2 and t % 3 == 0:
                        multiple_of_3 += 1
                else:
                    if (t1 <= t or t <= t2) and t % 3 == 0:
                        multiple_of_3 += 1
    print(multiple_of_3)