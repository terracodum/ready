def int32_to_ip(int32):
    n = bin(int32)[2::]
    if len(n) != 32:
        n = "0" * (32 - len(n)) + n
    return '{}.{}.{}.{}'.format(int(n[0:8:], 2), int(n[8:16:], 2), int(n[16:24:], 2), int(n[24:32:], 2))


print(int32_to_ip(2154959208))  # "128.114.17.104"
