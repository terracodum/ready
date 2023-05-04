for x in range(10):
    for y in range(1000):
        f = int("1" + str(x)+"2139"+str(y)+"4")
        if f % 2023 == 0:
            print(f,f//2023)
for k in range(10):
    f = int("1" + str(k) + "2139"  + "4")
    if f % 2023 == 0:
        print(f, f // 2023)
