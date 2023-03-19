counter = 0
even = [2, 4, 6, 8, 0]
for i in range(1000,10000):
    stri = str(i)
    flag = True
    for j in range(0, 4):
        if int(stri[j]) in even:
            flag = False
    num1 = int(stri[0]) + int(stri[1])
    num2 = int(stri[2]) + int(stri[3])
    array = [num1, num2]
    array = sorted(array)
    array = map(str,array)
    result = "".join(array)
    if result =="414" and flag:
        counter +=1
        print(i)
print(counter)