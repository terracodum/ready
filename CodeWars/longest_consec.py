def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k == 0:
        return ""
    res = []
    result = []
    for i in range(len(strarr) - k + 1):
        res.append([strarr[i + j] for j in range(k)])
    for j in res:
        resul = "".join(i for i in j)
        result.append(resul)
    lens = [len(i) for i in result]
    for i in result:
        if len(i)==max(lens):
            rur = i
            break
    return rur
