def f(n,m):
    if n == 10:
        return 0
    if n == m:
        return 1
    if n>m:
        return 0
    return f(n+1,m) +f(n*2,m)
def d(n,m):
    if n == 9:
        return 0
    if n == m:
        return 1
    if n > m:
        return 0
    return d(n+1,m) +d(n*2,m)
print(f(1,9)*f(9,20)+d(1,10)*d(10,20))
