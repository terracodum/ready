## 2
# print("x y z w")
# let = [0,1]
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 f = (not(y<=x)) or (z<= w) or (not(z))
#                 if f==0:
#                     print(x,y,z,w)

## 5
# for i in range(500):
#     bini = bin(i)[2::]
#     if bini.count("1") %2 ==0:
#         bini = "10" + bini[2::] + "0"
#     else:
#         bini = "11" + bini[2::] + "1"
#     num = int(bini,2)
#     if num > 40:
#         print(i , num)
## 8
# print(int("10000",8))
# print(int("100000",8))
# counter = 0
# for i in range(4096,32768):
#     oc = oct(i)
#     if oc.count("6") == 1 and (("16" not in oc) and ("36" not in oc) and ("56" not in oc) and ("76" not in oc) and ("96" not in oc)\
#         and ("61" not in oc) and ("63" not in oc) and ("65" not in oc) and ("67" not in oc) and ("69" not in oc)):
#         counter +=1
# print(counter)
## 9
# with open("X:\\Github\\some_files\\ege\\9.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
# for j in range(len(array)):
#     array[j] = list(map(int,array[j]))
# print(array)
## 24
with open("X:\\Github\\some_files\\new dxzz\\demo\\Доп.файлы\\fgf\\24.txt") as file:
    array = file.read()
i = 0
maxcount =0
counter =0
sog = "CDF"
glas = "AO"
while i < len(array):
    if array[i] in sog and array[i+1] in glas:
        counter +=1
        i +=2
    else:
        maxcount = max(maxcount, counter)
        i+=1
        counter = 0
print(maxcount)