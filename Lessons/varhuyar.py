#### 1
## 40

#### 2
# print("x y z w")
# let = [0, 1]
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 f = ((w <= y) <= (x == y)) or (not (z))
#                 if f == 0:
#                     print(x, y, z, w)
## xyzw

#### 3
## 989

#### 4
## 111

#### 5
# for n in range(500):
#     binn = bin(n)[2::]
#     if n % 3 == 0:
#         binn += binn[-3::]
#     else:
#         ost = bin((n%3)*3)[2::]
#         binn += ost
#     res = int(binn,2)
#     if res < 76:
#         print(n)
## 16

#### 6
##

#### 7
## 6720

#### 8
# let = "АВОРТ"
# counter = 0
# for a in let:
#     for b in let:
#         for c in let:
#             for d in let:
#                 for e in let:
#                     for f in let:
#                         fer = a+b+c+d+e+f
#                         counter+=1
#                         if fer=="ВОРОТА":
#                             print(counter)
## 4821

#### 9
# with open("X:\\Github\\some_files\\apoborodo\\9_8497.csv") as file:
#     array = [list(map(int, i.split(";"))) for i in file]
# print(len(array))
# counter = 0
# for j in range(len(array)):
#     if len(set(array[j])) == 5:
#         ren = sorted(array[j])
#         if 3 * (ren[0] + ren[-1]) >= 2 * (ren[1] + ren[2] + ren[3]):
#             counter+=1
#
# print(counter)
## 7695

#### 10
## 69

#### 11
## 4688

#### 12
# for n in range(3, 500):
#     string = "2" + "5" * n
#     while "25" in string or "355" in string or "555" in string:
#         if "25" in string:
#             string = string.replace("25", "5", 1)
#         if "355" in string:
#             string = string.replace("355", "52", 1)
#         if "555" in string:
#             string = string.replace("555", "3", 1)
#     if string.count("3") == 2:
#         print(n)
## 18

#### 13
## 33

#### 14
# for x in "0123456789ABCDE":
#     f = int("99658" + str(x) + "29", 15) + int("102" + str(x) + "023", 15)
#     if f % 14==0:
#         print(f//14)
## 118330623

#### 15
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f = ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))
#         if f == 0:
#             flag = False
#     if flag:
#         print(a)
## 16

#### 16
# def f(n):
#     if n>= 2025:
#         return n
#     if n < 2025:
#         return n+3+f(n+3)
# print(f(2018)-f(2022))
## 4049

#### 17
# with open("X:\\Github\\some_files\\apoborodo\\17_8504.txt") as file:
#     array = [int(i) for i in file]
#
# print(array)
# ars = []
# for j in range(len(array)):
#     if len(str(array[j])) == 3 and str(array[j])[-1] == "5":
#         ars.append(array[j])
# max_3 = min(ars)
# print(max_3)
# max_sum = 0
# counter = 0
# for i in range(len(array) - 1):
#     if (len(str(array[i])) == 3) or (len(str(array[i + 1])) == 3):
#         if (array[i] + array[i + 1]) % max_3 == 0:
#             counter += 1
#             max_sum = max(max_sum, array[i] + array[i + 1])
# print(counter, max_sum)
## 1 995

#### 18
## 2227 898

#### 19
# def game(first, step):
#     if first >= 55 or step > 2:
#         return step == 2
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#
# for i in range(1,55):
#     if game(i,0):
#         print(i)
## 18

#### 20
# def game(first, step):
#     if first >= 55 or step > 3:
#         return step == 3
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#
#
# #
#
# for i in range(1, 55):
#     if game(i, 0):
#         print(i)


## 614

#### 21
# def game(first, step):
#     if first >= 55 or step > 4:
#         return step == 2 or step == 4
#     if step % 2 == 0:
#         return all([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#
#
# for i in range(1, 55):
#     if game(i, 0):
#         print(i)
## 13

#### 22
## 51

#### 23
# def f(n, m):
#     if n == 12 or n > m:
#         return 0
#     if n == m:
#         return 1
#     else:
#         return f(n + 1, m) + f(n + 2, m) + f(n * 2, m)
#
#
# print(f(2, 9) , f(9, 17))
## 350

#### 24
with open("X:\\Github\\some_files\\apoborodo\\24_8510.txt") as file:
    array = file.read()
array = array.replace("N", "*")
array = array.replace("O", "*")
array = array.replace("P", "*")
counter = 0
while "**" in array:
    array = array.replace("**", "*-*")
    counter += 1

arrays = array.split("-")
arrays = list(map(len, arrays))
print(sorted(arrays)[-1])
## 58

#### 25
# for x in range(10):
#     for y in range(10):
#         f = int("12" + str(x) + str(y) + "15" + "6")
#         if f % 253 == 0:
#             print(f, f // 253)
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             f = int("12" + str(x) + str(y) + "15" + str(z) + "6")
#             if f%253 == 0:
#                 print(f,f//253)
# 1278156 5052
# 12531596 49532
# 12741586 50362
# 12951576 51192
