#### 1
## 45

#### 2
# print("x y z w")
# let = [0, 1]
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 f = (not (y and not(x))) and (not (x == z)) and w
#                 if f:
#                     print(x, y, z, w, )
## yxzw

#### 3
## 736

#### 4
## 110

#### 5
# for n in range(100):
#     binn = bin(n)[2::]
#     if n %3 == 0:
#         binn += binn[-3::]
#     else:
#         binn += bin((n%3)*3)[2::]
#     res = int(binn,2)
#     if res >76:
#
#         print(n)
## 11

#### 6
# from turtle import *
# speed(0)
# left(90)
# k = 25
# right(45)
# for i in range(7):
#     forward(6*k)
#     right(45)
#     forward(12*k)
#     right(135)
#
# up()
# for i in range(-1*k, 20 *k,k):
#     for j in range(-1*k, 20 *k,k):
#         goto(i,j)
#         dot(3)
# done()
## 44

#### 7
## 44

#### 8
# let = "AКЛМНЯ"
# counter = 0
# for a in let:
#     for b in let:
#         for c in let:
#             for d in let:
#                 for e in let:
#                     string = a + b + c + d + e
#                     counter += 1
#                     if string[0] == "К" and string[1] == "М":
#                         print(counter)
## 1945

#### 9
# with open("X:\\Github\\some_files\\navar\\9_7611.csv") as file:
#     array = [list(map(int, i.rstrip().split(";"))) for i in file]
# print(array)
# counter  =0
# for i in range(len(array)):
#     if len(set(array[i])) == 5:
#         ars = array[i]
#         ars = sorted(ars)
#         if (ars[0] + ars[-1]) * 2 >= ars[1] + ars[2]+ ars[3]:
#             counter+=1
# print(counter)
## 15058

#### 10
## 58 -16 = 42

#### 11
## 294

#### 12
# for i in range(4,10000):
#     string = "3" +"5"*i
#     while "25" in string or "355" in string or "555" in string:
#         if "25" in string:
#             string = string.replace("25", "32", 1)
#         if "355" in string:
#             string = string.replace("355", "25", 1)
#         if "555" in string:
#             string = string.replace("555", "3", 1)
#     array = [int(i) for i in string]
#     if sum(array) == 17:
#         print(i)
## 26

#### 13
## 23

#### 14
# for x in "0123456789ABCDE":
#     f = int("97968" + str(x) +"15" , 15)  + int("7" + str(x)+ "233",15)
#     if f %14 == 0:
#         print(x, f/14)
## 116071912

#### 15
# for a in range(500):
#     flag =  True
#     for x in range(500):
#         for y in range(500):
#             f = (x>=9) or (2*x < y) or (x*y < a)
#             if f==0:
#                 flag = False
#     if flag:
#         print(a)
##129

#### 16
# def f(n) :
#     if n >= 2025:
#         return n
#     if n <2025:
#         return n + f(n+2)
# print(f(2022)-f(2023))
## 2024

#### 17
# with open("X:\\Github\\some_files\\navar\\17_7619.txt") as file:
#     array = [int(i) for i in file]
# print(array)
# max_2 = []
# for j in range(len(array)):
#     if len(str(array[j])) == 2:
#         max_2.append(array[j])
# counter = 0
# max_count = 0
# max2 = max(max_2)
# for i in range(len(array) - 1):
#     if (len(str(array[i])) == 2 and len(str(array[i + 1])) != 2) or (
#             len(str(array[i + 1])) == 2 and len(str(array[i])) != 2):
#         if (array[i] + array[i + 1]) % max2 == 0:
#             counter += 1
#             max_count = max(max_count, array[i] + array[i + 1])
# print(counter,max_count)
## 1 2970

#### 18
# 2341 954

#### 19
# def game(first, step):
#     if step > 2 or first >= 43:
#         return step == 2
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
# for i in range(1,43):
#     if game(i,0):
#         print(i)
## 14

#### 20
# def game(first, step):
#     if step > 3 or first >= 43:
#         return step == 3
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
# for i in range(1,43):
#     if game(i,0):
#         print(i)
## 14 38

#### 21
# def game(first, step):
#     if step > 4 or first >= 43:
#         return step == 2 or step == 4
#     if step % 2 == 0:
#         return all([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 4, step + 1), game(first * 3, step + 1)])
# for i in range(1,43):
#     if game(i,0):
#         print(i)
## 9

#### 22
## 79

#### 23
# def f(n,m):
#     if n == 11:
#         return 0
#     if n>m:
#         return 0
#     if n==m:
#         return 1
#     else:
#         return f(n+1,m) + f(n*2,m) +f(n*3,m)
# print(f(2,15),f(15,25))
## 12

#### 24
# # print(array)
# with open("X:\\Github\\some_files\\navar\\24_7624.txt") as f:
#     array = f.read()
# array = array.replace("X","*")
# array = array.replace("Y","*")
# array = array.replace("Z","*")
# array = array.replace("**", "* *")
# array = array.split()
# arrays = list(map(len,array))
# print((sorted(arrays))[-1])


##111

##### 25
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             f = int("11" + str(x) + str(y)+ "4"+str(z)+"56",10)
#             if f % 211 == 0:
#                 print(f, f//211)
# for x in range(10):
#     for y in range(10):
#         f = int("11" + str(x) + str(y)+"4"+"56",10)
#         if f % 211 == 0:
#             print(f, f//211)

#### 27
# with open("X:\\Github\\some_files\\navar\\27_B_7627.txt") as file:
#     serv = int(file.readline())
#     array = [int(i) for i in file]
#
# max_sum = 0
# for i in range(len(array)-1):
#     if i == len(array):
#         ars = 0
#     if len(array)< i+serv+1:
#         ars = max(array[i+1::])
#     else:
#         ars = max(array[i+1:i+serv+1:])
#     max_sum = max(ars+array[i],max_sum)
#
# print(max_sum)
