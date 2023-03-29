def expanded_form(num):
    result = []
    num1 = str(num)[::-1]
    for i in range(len(num1)):
        if num1[i]=="0":
            continue
        else:
            num2 = num1[i] + "0"*i
            result.append(num2)
            result.append(" + ")
            print(result)
    result.reverse()
    res = "".join(result)
    return res[3::]
print(expanded_form(70304))
