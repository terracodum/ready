def spin_words(sentence):
    sens = sentence.split()
    res = ""
    print(sens)
    if len(sens) == 1 and len(sens[0]) >= 5:
        res = sens[0][::-1]
    elif len(sens) == 1 and len(sens[0]) <= 5:
        res = sens[0]
    else:
        for i in sens:
            if len(i) >= 5:
                sel = i[::-1]
                res = res + " " + sel
            else:
                res = res + " " + i
        res = res[1::]
    return res


print(spin_words("This sentence is a sentence"))
