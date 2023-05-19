## 2
# print("x y z w")
# let = [0,1]
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 f =(x and y) or (y == z) or w
#                 if f == 0:
#                     print(x, y, z, w)
## 5
# for i in range(100,1000):
#     stri = str(i)
#     n1 = int(stri[0]) + int(stri[1])
#     n2 = int(stri[1]) + int(stri[2])
#     res =  str(min(n1,n2))+ str(max(n1,n2))
#
#     if res == "1115":
#         print(i)
## 8
# let = "АВС"
# counter = 0
# lef = "АВСХ"
# for a in let:
#     for b in let:
#         for c in let:
#             for d in let:
#                 for e in lef:
#                     string = a +b +c +d + e
#                     if string.count("Х") <= 1:
#                         counter+=1
# print(counter)
## 14
# num = (4**16) + (2**36) - 8
# bit = bin(num)[2::]
#
# print(bit.count("1"))
## 16
# def f(n):
#     if n == 0:
#         return 0
#     if n>0 and n%2==0:
#         return f(n/2)
#     if n>0 and n%2 ==1:
#         return 1 + f(n-1)
# for i in range(10000000000):
#     if f(i)==11:
#         print(i)
## 17
# with open("C:\\Users\\nikit\\Downloads\\178343.txt") as file:
#     array = [int(i) for i in file]
# mie = 1000000000000000000
# for j in range(len(array)):
#     if len(str(array[j])) == 3 and array[j] % 10 == 5:
#         mie = min(mie, array[j])
# print(mie)
# arrays = []
# for k in range(100,1000):
#     arrays.append(k)
# print(arrays)
#
# minsum = 10000000000000000000000
# counter = 0
# for i in range(len(array) - 1):
#     if (array[i] in arrays and array[i+1] not in arrays) or (array[i] not in arrays and array[i+1] in arrays):
#         if (array[i] + array[i + 1]) % mie == 0:
#             counter += 1
#             minsum = min(minsum, array[i] + array[i + 1])
# print(counter, minsum)
## 19
# def game(first, step):
#     if step > 2 or first >= 74:
#         return step == 2
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,74):
#     if game(i,0):
#         print(i)
## 20
# def game(first, step):
#     if step > 3 or first >= 74:
#         return step == 3
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,74):
#     if game(i,0):
#         print(i)
## 21

# def game(first, step):
#     if step > 4 or first >= 74:
#         return step == 2 or step==4
#     if step % 2 == 0:
#         return all([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,74):
#     if game(i,0):
#         print(i)
## 23
# def f(x,y):
#     if x> y or x== 18:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+1,y)+f(x*2,y)
# print(f(1,10)*f(10,21))
# 25
# def dels(n):
#     array = []
#     for i in range(1,int(n**0.5)+1):
#         if n%i ==0:
#             array.append(i)
#             array.append(n//i)
#     return array
# maxlen = 0
# maxs = 0
# for i in range(120115,120201):
#     ars = sorted(dels(i))
#     maxlen = max(maxlen,len(ars))
#     if maxlen == len(ars):
#         maxs = i
# print(maxlen,maxs)
## 24
# with open("C:\\Users\\nikit\\Downloads\\24_demo.txt") as file:
#     array = file.read()
# counter = 1
# maxcount = 0
# for i in range(len(array)-1):
#     if array[i] != array[i+1]:
#         counter+=1
#     else:
#         maxcount = max(maxcount,counter)
#         counter=1
# maxcount = max(maxcount,counter)
#
# print(maxcount)#######
##########################
## 2
# let = [0,1]
# print("x y z w")
# for x in let:
#     for y in let:
#         for z in let:
#             for w in let:
#                 f = (x and (not(y))) or (x == z) or (not(w))
#                 if f ==0:
#                     print(x, y, z, w)
## 5
# for n in range(1000):
#     binn = bin(n)[2::]
#     if n%2 == 0:
#         binn+= "10"
#     else:
#         binn+="01"
#     res= int(binn,2)
#     if res <= 102:
#         print(n , res)
## 8
# sog = "ГД"
# glas = "О"
# all = "ГДО"
# counter = 0
# for a in sog:
#     for b in all:
#         for c in all:
#             for d in all:
#                 for e in all:
#                     for f in sog:
#                         f = a+ b +c + d + e+ f
#                         counter +=1
# print(counter)
## 12
# string = "1" + "0"*80
# while ("10" in string) or ("1" in string):
#     if "10" in string:
#         string.replace("10","001",1)
#     elif "1" in string:
#         string.replace("1","000")
# print(string.count("0"))
# s = '1' + '0' * 80
# while ('10' in s) or ('1' in s):
#     if '10' in s:
#         s = s.replace('10', '001', 1)
#     elif '1' in s:
#         s = s.replace('1', '000')
# print(s.count('0'))
def f(x):
    k=2
    deliteli=set()
    while k * k <= x:
        if x % k==0:
            deliteli.add(k)
            if x // k < x:
                deliteli.add(x // k)
        k = k + 1
    return sorted(deliteli)
start = 174457
end = 174505
for i in range(start, end + 1):
    if len(f(i)) == 2:
        print(f(i))