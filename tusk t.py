letters = "СВЕТ"
letters = sorted(letters)
result = ""
counter = 0
exitflag = False
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        result = a + b + c + d + e + f
                        counter += 1
                        if result[0] == "Т":
                            print(counter, result)

                            exitflag = True
                            break
                    if exitflag:
                        break
                if exitflag:
                    break
            if exitflag:
                break
        if exitflag:
            break
    if exitflag:
        break
