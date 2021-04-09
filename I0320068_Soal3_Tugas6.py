n = 99
for j in range(1, n + 1):
    if j > 1:
        for i in range(2,j):
            if (j % i) == 0:
                print(j, "bukan bilangan prima")
                break
        else:
            print(j, "adalah bilangan prima")