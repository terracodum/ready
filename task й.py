def solution(s):
    indexi = []
    flag = False
    for i in range(len(s)):
        sl = s[i:]
        finder = sl[0].isupper()
        if finder:
            indexi.append(i)
            flag = True
        else:
            continue
    if flag:
        oldj = 0
        res = ""
        for j in indexi:
            print(j, oldj)
            sR = s[oldj:j:]
            res += " " + "".join(sR)

            oldj = j
        res = res + " " + "".join(s[oldj::])
        return res
    else:
        return s