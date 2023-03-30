def f(n, m, flag):
    if n == m:
        return 1
    if n >= m:
        return 0
    if flag:
        return f(n + 1, m, True) + f(n + 2, m, True) + f(n * 2, m, False)
    else:
        return f(n+1,m ,True) + f(n+2,m ,True)
print(f(1,9 ,True))