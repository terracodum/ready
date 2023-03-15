letters = "ВАЛЕРИЯ"
letters = sorted(letters)
exitflag = False
result = ""
counter = 0
for a in letters:
    for b in letters:
        for c in letters:
            result = a + b + c
            if result.count("В")==1:
                counter+=1
                if result.count("А")==0:
                    exitflag = True
                    break
        if exitflag:
            break
    if exitflag:
        break
print(counter, result)
