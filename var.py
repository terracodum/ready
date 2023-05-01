# print("x y z w")
# lit = [0,1]
# for x in lit:
#     for y in lit:
#         for z in lit:
#             for w in lit:
#                 F = (x or y) and (not(y == z)) and not(w)
#                 if F :
#                     print(x, y , z ,w)
#######################################
# lit = [1,3,5,7,9]
# counter = 0
# for a in lit:
#     for b in lit:
#         for c in lit:
#             for d in lit:
#                 num1 = a+b
#                 num2 = c+d
#                 num3 = str(min(num1,num2)) + str(max(num1,num2))
#                 print(num1,num2,num3)
#                 if num3 == '616':
#                     counter+=1
# print(counter)
#############################
# count = 0
# maxsum = 0
# f = open('C:\\Users\\nikit\\Downloads\\17.txt')
# l = [int(i) for i in f]
# f.close()
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] % 34 != 0:
#             count += 1
#             maxsum = max(maxsum, l[i] + l[j])
# print(count, maxsum)
#######################
# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x + 4, y)
# print(f(1, 8) * f(8, 15))
#############################
# for a in range(100, 0, -1):
#     k = 0
#     for x in range(1, 1000):
#         if (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0))):
#             k += 1
#     if k == 999:
#         print(a)
#         break
############################################ 16.04.23 ###############################################
##  №2
# print("x y z w")
# let = [0,1]
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 F = (not((not(z) or w) and (not(x) == y)) or (x and z))
#                 if F == 0:
#                     print(x, y, z, w)
##  №5
# for n in range(10000):
#     m = n
#     b = ''
#     while n > 0:
#         b = str(n % 3) + b
#         n = n // 3
#     b = b + str(m%3)
#     res = int(b,3)
#     if len(str(res))==4:
#         print(res)
##  №8
# let = "ВИШНЯ"
# counter = 0
# for a in let:
#     for b in let:
#         for c in let:
#             for d in let:
#                 for e in let:
#                     for f in let:
#                         sen = a + b + c + d + e + f
#                         if sen[0]!= "Ш" and sen[-1]!="И" and sen[-1]!="Я" and sen.count("В")<=1:
#                             counter +=1
# print(counter)
##  №12
# let = "1"+("9"*100)
# while ("19" in let) or ("299" in let) or ("3999" in let):
#     let = let.replace("19","2",1)
#     let = let.replace("299","3",1)
#     let = let.replace("3999","1",1)
# print(let)
##  №14
# num = (9**12) + (3**8) - 3
# m = num
# b = ''
# while num > 0:
#     b = str(num % 3) + b
#     num = num // 3
# print(b.count("2"))
##  №15

# for A in range(300, -1, -1):
#     k = 0
#     for x in range(1, 301):
#         for y in range(1, 301):
#             if (x * y < 140) or (y > A) or (x > A):
#                 k += 1
#     if k == 90000:
#         print(A)
#         break
##  #16
# def f(n):
#     if n ==1:
#         return 3
#     if n == 2:
#         return 3
#     if n >2:
#         return 5*(f(n-1)) - 4*(f(n-2))
# print(f(15))
##  #17
# with open("C:\\Users\\nikit\\Downloads\\12312.txt") as file:
#     array = [int(i) for i in file]
# maxar = 0
# for i in array:
#     if i %10 == 3:
#         maxar = max(maxar,i)
# counter = 0
# maxsum = -111111111111111111111111111111
# for i in range(len(array)-1):
#     if ((str(array[i])[-1]=="3") and (str(array[i+1])[-1]!="3")) or ((str(array[i])[-1]!="3") and (str(array[i+1])[-1]=="3")):
#         if (array[i]**2) + (array[i+1]**2) >= maxar**2:
#             maxsum = max(maxsum,(array[i]**2)+(array[i+1]**2))
#             counter+=1
# print(counter,maxsum)
## # 24
# with open("C:\\Users\\nikit\\Downloads\\24.txt") as file:
#     array = file.read()
# array = array.split("A")
# print(array)
# array.pop(0)
# array.pop(-1)
# counter = 0
# for i in range(len(array)):
#     if len(array[i])>=8:
#         if "B" not in array[i]:
#             counter+=1
# print(counter)
##  №18
# with open("X:\\Github\\some_files\\80.csv") as file:
#
#     array = [float(i.rstrip().replace(",",".")) for i in file]
# maxsum = -100000000000000000000000
# curent = 0
# for i in range(len(array)-1):
#
#     if abs(array[i]-array[i+1])<=10:
#         curent += array[i]
#         maxsum = max(maxsum,curent)
#     else:
#         curent += array[i]
#         maxsum= max(maxsum,curent)
#         curent=0
#
# print(maxsum)
#
##########################################################1 15
# for i in range(1, 100):
#     s = bin(i)[2:]
#     s = str(s)
#     s = s[s.find('1'):]
#     if s.count('1') > s.count('0'):
#         s += '1'
#     else:
#         s += '0'
#     result = int(s, 2)
#     if result > 100:
#         print(result)
#         break
############################
# s = '1' * 82
# while ('11111' in s) or ('888' in s):
#     if '11111' in s:
#         s = s.replace('11111', '88', 1)
#     elif '888' in s:
#         s = s.replace('888', '8', 1)
# print(s)
#############################
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return F(n - 2) * (n - 1)
# print(F(7))
############################
# with open("C:\\Users\\nikit\\Downloads\\17 (3).txt") as file:
#     array = [int(i) for i in file]
# count = m = 0
# for i in range(len(array) - 1):
#     for j in range(i + 1, len(array)):
#         if (array[i] + array[j]) % 10 == 0:
#             count += 1
#             m = max(m, array[i] + array[j])
# print(count, m)
###################################
# def f(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 2, y) + f(x * 2, y)
# print(f(1, 18) * f(18, 52))
#######################################
# with open("C:\\Users\\nikit\\Downloads\\24 (1).txt") as file:
#
#     st = file.readline()
# k = 1
# mx = 0
# for i in range(1, len(st)):
#     if (st[i] == 'K' and st[i-1] == 'L') or (st[i-1] == 'K' and st[i] == 'L'):
#         k = 1
#     else:
#         k += 1
#         if k > mx:
#             mx = k
# print(mx)
########################################
# def game(first,step):
#     if first >=26 or step>4:
#         return step == 2 or step == 4
#     if step % 2 == 0:
#         return all([game(first+1, step+1),game(first*2,step+1)])
#     else:
#         return any([game(first+1, step+1),game(first*2,step+1)])
# for i in range(1,26):
#     if game(i,0):
#         print(i, end=" ")
############################################
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not((x == (not(y))) <= ((x and w) == (z and not(w)))):
#                     print(x, y, z, w)