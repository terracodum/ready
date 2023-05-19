def hex_string_to_RGB(hex_string):
    value = hex_string.lstrip('#')
    lv = len(value)
    a = list(tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))
    stri = "rgb"
    res = {}
    for i in range(len(a)):
        res.setdefault(stri[i], a[i])
    return res


print(hex_string_to_RGB("#00FF7D"))

