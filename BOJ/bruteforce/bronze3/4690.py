for i in range(2, 101):
    for j in range(2, i):
        for k in range(j, i ):
            for l in range(k, i):
                if i ** 3 == j ** 3 + k ** 3 + l ** 3:
                    print("Cube = %d, Triple = (%d,%d,%d)" % (i, j, k, l))