def rgb(r, g, b):
    colors = [r, g, b]
    res = ""
    for i in colors:
        col = hex(i)[2::]
        if i < 0:
            col = "00"
        if i > 255:
            col = "FF"
        if len(col) < 2:
            col = "0" + str(col)
        res += col
    return res.upper()
