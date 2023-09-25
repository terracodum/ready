## 2
# let = [0,1]
# print("x y z w")
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 f = (x and not(y)) or (y == z) or (not(w))
#                 if f ==0:
#                     print(x,y,z,w)
## 5
# for n in range(10000):
#     binn = bin(n)[2::]
#     if n % 3 == 0:
#         binn = binn + binn[-3::]
#     else:
#         binn = binn + str(bin((n % 3)*3)[2::])
#     res = int(binn,2)
#     if res <100:
#         print(n)
# 6
# import turtle
# turtle.speed(0)
# turtle.left(90)
# turtle.right(315)
# k = 10
# turtle.color("Black", "Green")
# turtle.begin_fill()
# for i in range(7):
#     turtle.forward(16*k)
#     turtle.right(45)
#     turtle.forward(8*k)
#     turtle.right(135)
# turtle.end_fill()
# turtle.up()
# canvas = turtle.getcanvas()
# counter = 0
# for i in range(-30 * k, 30 * k, k):
#     for j in range(-30 * k, 30 * k, k):
#         root = canvas.find_overlapping(i, j, i, j)
#         print(root)
#         if len(root) == 1 and root[0] == 5:
#             counter += 1
#
# print(counter)
# turtle.done()
##8
# let = "АВЛОР"
# counter  = 0
# for a in let:
#     for b in let:
#         for c in let:
#             for d in let:
#                 f = a+b+c+d
#                 counter+=1
#                 if f[0] == "Л" :
#                     print(counter)
##9
# with open("X:\\Github\\some_files\\demo\\09.csv") as file:
#     array = [i.rstrip() for i in file]
# ar = []
# print(array)
# for i in range(len(array)):
#     array[i] = list(map(int,(array[i].split(";"))))
# print(array)
# counter  =0
# for i in range(len(array)):
#     array[i] = sorted(list(set(array[i])))
#     if len(array[i]) == 5:
#         if 3*(array[i][-1]+ array[i][0]) <= 2*(array[i][1]+array[i][2]+array[i][3]):
#             counter+=1
# print(counter)
## 12
# for i in range(4,100):
#     string = "3" + "5"*i
#     while "25" in string or "355" in string or "555"in string:
#         if "25" in string:
#             string = string.replace("25","3",1)
#         if "355" in string:
#             string = string.replace("355", "52",1)
#         if "555" in string:
#             string= string.replace("555","23",1)
#     sum_str = 0
#     for  j in range(len(string)):
#         sum_str += int(string[j])
#     if sum_str == 27:
#         print(i)
## 14
# for x in "0123456789ABCDE":
#     f = int("97968"+ str(x)+"13",15) + int("7"+str(x)+"213",15)
#     if f % 14 ==0 :
#         print(f//14)
## 15
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f = (x&39 ==0) or ((x&11 ==0) <= (not(x&a==0)))
#         if f ==0 :
#             flag = False
#     if flag:
#         print(a)
##16
# def f(n):
#     if n >=2025:
#         return n
#     if n<2025:
#         return n+3+f(n+3)
# print(f(23) - f(21))
## 17
# with open("X:\\Github\\some_files\\demo\\17_7596.txt") as file:
#     array = [int(i) for i in file]
# min_se = []
# for j in range(len(array)):
#     if len(str(array[j])) == 3:
#         if str(array[j])[-1] =="5":
#             min_se.append(array[j])
# min_sum = min(min_se)
# counter  =0
# min_s = 0
# for i in range(len(array)-1):
#     if (len(str(array[i]))==3 and len(str(array[i+1]))!=3) or (len(str(array[i]))!=3 and len(str(array[i+1]))==3):
#         if (array[i] + array[i+1]) % min_sum == 0:
#             counter+=1
#             min_s =max(min_sum, array[i] + array[i+1])
# print(counter,min_s)
# 19 20 21
# def game(first,step):
#     if first >= 78 or step > 2:
#         return step == 2
#     if step % 2 == 0:
#         return all([game(first+1,step+1), game(first+4,step+1), game(first*4,step+1)])
#     else:
#         return any([game(first+1,step+1), game(first+4,step+1), game(first*4,step+1)])
# for i in range(1,78):
#     if game(i,0):
#         print(i)
## 23
# def f(a,b):
#     if a > b or a == 13:
#         return 0
#     if a == b :
#         return 1
#     else:
#         return f(a+1,b) + f(a+2,b) + f(a*3,b)
# print(f(3,8)*f(8,18))
## 24
# with open("X:\\Github\\some_files\\demo\\24_7600.txt") as file:
#     array = file.read()
# print(array)
# counter = 1
# max_count = 0
# for i in range(1,len(array)):
#     if array[i] in "QRS" and array[i-1] in "QRS":
#         max_count = max(max_count,counter)
#         counter=1
#     else:
#         counter+=1
#         max_count = max(max_count,counter)
# print(max_count)
## 25
# for x in range(10):
#     for z in range(10):
#         for y in range(10):
#             num = int("12" + str(x) + str(z) + "36" + str(y) + "1")
#             if num % 273 == 0:
#                 print(num, num // 273)
# for x in range(10):
#     for z in range(10):
#         num = int("12" + str(x) + str(z) + "36" + "1")
#         if num % 273 == 0:
#             print(num, num // 273)
