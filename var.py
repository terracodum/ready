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
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0))):
            k += 1
    if k == 999:
        print(a)
        break