# def de(x,a):
#     return x % a == 0
#
#
# for a in range(1,500):
#     flag = True
#     for x in range(1,500):
#         F = de(120,a) and (de(x,36) <= (de(x,a) or not(de(x,45))))
#         if F:
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
# ###########################################################################
# for a in range(1,500):
#     flag = True
#     for x in range(1,500):
#         for y in range(1,500):
#             f = ((x<= 0)<=(x*x<=a)) and ((y*y<=a)<=(y<=9))
#             if f == False:
#                 flag = False
#                 break
#     if flag:
# #         print(a)
# ##################################################################################
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         f = (x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))
#         if f:
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
###########################################################
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         f = ((x&28!=0)or(x&45!=0)) <= ((x&48==0) <=(x&a!=0))
#         if f:
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
######################################################## 30.04.23
## 1
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         f = (x&29!=0) <= ((x&12==0) <= (x&a != 0))
#         if f:
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
## 2
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         f = ((x&28!=0)or(x&45!=0)) <= ((x&17==0)<=(x&a!=0))
#         if f:
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
## 5
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         for y in range(1,500):
#             f = ((x * y)<a) or (x<y) or (x>=12)
#             if f:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
## 6
# counter = 0
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         for y in range(1,500):
#             f = ((x<=5) <= (x**2<=a)) and ((y**2 <= a )<=(y<=5))
#             if f:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
#         counter +=1
# print(str(counter) + " dg")
## 7
# counter = 0
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         for y in range(1,500):
#             f = ((x<=9) <= (x**2<=a)) and ((y**2 <= a )<=(y<=9))
#             if f:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
## 9
# def de(m,n):
#     return m%n==0
# for a in range(1,500):
#     flag =  True
#     for x in range(1,500):
#         for y in range(1,500):
#             f = ((3*x + 4*y )!= 60) or ((a>=x)and(a>=y))
#             if f:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
#         break
