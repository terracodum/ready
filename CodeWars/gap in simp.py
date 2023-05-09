def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
array =[]
def gap(g, m, n):
    for i in range(m,n+1):
        if is_simple(i):
            array.append(i)
    for j in range(len(array)-1):
        for k in range(j+1,len(array)):
            if array[k] - array[j] == g:
                return [array[j], array[k]]



print(gap(10,300,400))