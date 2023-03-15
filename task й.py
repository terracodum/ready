letters = "ЛЕВИЙ"
letters = sorted(letters)
result = ""
counter = 0
exitflag = False
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    # for f in letters:
                    result = a + b + c + d + e
                    if result[0]!="Й" and result.count("Л")==1 and result.count("Е")==1 and result.count("В")==1 \
                        and result.count("И")==1 and result.count("Й")==1 and result.count("ЕИ")==0:
                        counter +=1
print(counter) 