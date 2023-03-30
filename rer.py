def f(n,m):
    if n == 12 or n==11:
        return 0
    if n ==m:
        return 1
    if n >= m:
        return 0
    return f(n+1,m) + f(n+2,m) +f(n*3,m)
print(f(1,9)*f(9,30))
