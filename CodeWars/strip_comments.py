def strip_comments(strng, markers):
    if "\t" in strng:
        strng = strng.replace("\t","\n")
    array = strng.split("\n")
    for i in range(len(array)):
        for j in markers:
            if j in array[i]:
                indexa = array[i].index(j)
                array[i] = array[i][:indexa:]
                for k in array[i]:
                    if array[i][-1] == " ":
                        array[i] = array[i][:-1:]
    res = ""
    for i in range(len(array)):
        if len(array) == i +1:
            res += array[i]
        else:
            res += array[i]+ "\n"
    return res

print(strip_comments('\t=\n# ^ !\n# . lemons\ncherries avocados\n@ oranges lemons watermelons @', [',', '#', '=']))