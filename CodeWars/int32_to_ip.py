def int32_to_ip(int32):
    n = bin(int32)[2::]
    if len(n) < 32:
        t = 32 - len(n)
        n = "0" * t + n
    for i in range(4):
        n1 = int(n[0:8:], 2)
        n2 = int(n[8:16:], 2)
        n3 = int(n[16:24:], 2)
        n4 = int(n[24:32:], 2)
    return n1, n2, n3, n4


print(int32_to_ip(2154959208))  # "128.114.17.104"
print(bin())
