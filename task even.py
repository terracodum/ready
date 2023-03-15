letters = "01234567"
letters = sorted(letters)
even = "024"
odd = "1357"
print(letters)
result = ""
counter = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
            #         for f in letters:
            # #             for g in  letters:
            # #                 for h in letters:
                    result = a + b + c + d + e

                    if result.count("6")==1 and result[0]=="6" and result[1] in even :

                        counter +=1
                    elif result.count("6")==1 and result[-1]=="6" and result[-2] in even and result[0]!="0":
                        counter +=1
                    elif result.count("6")==1 and result[0] != "0":
                        indexres = result.index("6")
                        if result[indexres - 1] in even and result[indexres + 1] in even:
                            counter += 1
                            break
print(counter)
