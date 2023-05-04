def dels(n):
    array = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            array.append(i)
            array.append(n // i)
    return array
def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
## 1
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f = (x&41 != 0) <= ((x&33 == 0 )<= (x&a !=0))
#         if f:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(a)
## 3
# for a in range(500):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             f = (x<=9) <= (x**2 <=a) and (y**2<=a)<=(y<=9)
#             if f:
#                 pass
#             else:
#                 flag = False
#     if flag:
#         print(a)
## 5
# def de(n,m):
#     return n%m==0
# for a in range(1,500):
#     flag = True
#     for x in range(1,500):
#         f = (a<50) and (de(x,a) or (de(x,10) <= (not(de(x,18)))))
#         if f:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(a)
## 6

# for i in range(174457,174506):
#
#     if len(dels(i))==2:
#         print(i, dels(i))

## 7
# for i in range(312614,312652):
#     if len(dels(i))==6:
#         print(i ,dels(i))
## 8
# for i in range(95632,95651):
#     ars = dels(i)
#     count = 0
#     for j in range(len(ars)):
#         if ars[j]%2!=0:
#             count+=1
#     if count == 6:
#         print([k for k in ars if k%2!=0])
## 9
# max_dels = 0
# max_num = 0
# for i in range(120115,120200):
#     ars = dels(i)
#     if max_dels <= len(ars):
#         max_dels = len(ars)
#         max_num = i
# print(max_dels,max_num)
## 10
for i in range(289123456,389123457):
    if (round(i**0.5)) == i**0.5:
        ars = dels(i)
        if len(ars)==3:
            print(sorted(ars),i)
##11
# def dels10(n):
#     array = []
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             array.append((n//i) - i)
#     return array
# ary = []
# for i in range(1000000, 2000001):
#
#     ars= dels10(i)
#     counter = 0
#     for j in range(len(ars)):
#         if ars[j] <=100:
#             counter+=1
#
#     if counter>=3:
#         ary.append(i)
# print(ary)
##12
# counter = 0
# for i in range(700000,10000000000000000000):
#     ars = dels(i)
#
#     if counter == 5:
#         exit()
#     if len(ars)>=2:
#         m = ars[0]+ars[-1]
#     else:
#         m=0
#     if m%10==8:
#         counter+=1
#
#         print(i, m)
#
#
