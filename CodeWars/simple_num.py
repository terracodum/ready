def simple_num(a):
    for i in range(2, (a // 2) + 1):
        if a % i == 0:
            return False
    return True
