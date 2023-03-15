letters = "01234567"
even = "0246"
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
                        if (result[0]<result[2] and result[0]<result[3] \
                            and result[0]<result[4] and result[0]<result[5]) \
                            and (result[1]<result[2] and result[1]<result[3] \
                            and result[1]<result[4] and result[1]<result[5]):
                                for i in range(0,4):
                                    counter +=1
                                    print(counter)