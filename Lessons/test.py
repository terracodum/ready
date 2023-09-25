#### 1
# def game(first, step):
#     if step > 2 or first >= 51:
#         return step == 2
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,51):
#     if game(i,0):
#         print(i)
## 6

#### 2
# def game(first, step):
#     if step > 3 or first >= 51:
#         return step == 3
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,51):
#     if game(i,0):
#         print(i)
## 14 15

#### 3
# def game(first, step):
#     if step > 4 or first >= 51:
#         return step == 4 or step == 2
#     if step % 2 == 0:
#         return all([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,51):
#     if game(i,0):
#         print(i)
## 13

#### 4
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f = (x&29 != 0) <= ((x&12 == 0)<=(x&a != 0))
#         if f == 0:
#             flag = False
#     if flag:
#         print(a)
## 17

#### 5
# def is_simple(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# l = 0
# for n in range(2422000, 2422081):
#     if  is_simple(n):
#         l+=1
#         print(l,n)
## 1 2422027
## 2 2422033
## 3 2422037
## 4 2422073

#### 6
# def is_sqr(j):
#     if (round(j**0.5))**2 == j:
#         return True
#     else:
#         return False
# def dels(n):
#     res = []
#     for i in range(2, 1 + int(n ** 0.5)):
#         if n % i == 0:
#             res.append(i)
#             res.append(n // i)
#     return sorted(list(set(res)))
# for n in range(289123456, 389123457):
#     if is_sqr(n):
#         lel = dels(n)
#         if len(lel) == 3:
#             print(n,lel[-1])
## 294499921 2248091
## 352275361 2571353
## 373301041 2685619

#### 7
# def dels(n):
#     res = []
#     for i in range(1, 1 + int(n ** 0.5)):
#         if n % i == 0:
#             res.append(i)
#             res.append(n // i)
#     return sorted(list(set(res)))
#
# res = []
# for i in range(600000, 1000000000000000000):
#
#     ror = dels(i)
#     for j in range(len(ror)):
#         if ror[j] != 7 and ror[j] != i:
#             if str(ror[j])[-1] == "7":
#                 res.append([i, ror[j]])
#                 break
#     print(*res)
#     if len(res) == 5:
#         break
## [600001, 437] [600002, 47] [600003, 1227] [600005, 217] [600012, 16667]

#### 8
# def game(first, step):
#     if step > 2 or first >= 65:
#         return step == 2
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,65):
#     if game(i,0):
#         print(i)
## 8

#### 9
# def game(first, step):
#     if step > 3 or first >= 65:
#         return step == 3
#     if step % 2 == 0:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return all([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,65):
#     if game(i,0):
#         print(i)
## 7 19 20

#### 10
# def game(first, step):
#     if step > 4 or first >= 65:
#         return step == 4 or step == 2
#     if step % 2 == 0:
#         return all([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
#     else:
#         return any([game(first + 1, step + 1), game(first + 2, step + 1), game(first * 3, step + 1)])
# for i in range(1,65):
#     if game(i,0):
#         print(i)
## 18

#### 11
# string = ">" + "1" * 26 + "2" * 10 + "3" * 14

## no answer

#### 12
# for i in range(3,500):
#     bini = bin(i)[2::]
#     bini = bini + bini[1] + bini[0]
#     res = int(bini,2)
#     if res>90:
#         print(i)
## 23

#### 13
# for i in range(128, 256):
#     bini = bin(i)[2::]
#     bini = bini.replace("1", "*")
#     bini = bini.replace("0", "1")
#     bini = bini.replace("*", "0")
#     res = i - int(bini,2)
#     if res == 185:
#         print(i)
## 220

#### 14
# for i in range(3,1000000):
#     bini = bin(i)[2::]
#     bini = bini.replace("1", "*")
#     bini = bini.replace("0", "1")
#     bini = bini.replace("*", "0")
#     res = i - int(bini,2)
#     if res == 999:
#         print(i)
## 1011

#### 15
# def dels(n):
#     res = []
#     for i in range(2, 1 + int(n ** 0.5)):
#         if n % i == 0:
#             res.append(i)
#             res.append(n // i)
#     return sorted(list(set(res)))
# res = []
# j = 0
# for i in range(200_000_001,200_000_000_000):
#     if len(res) == 5:
#         break
#     rel = dels(i)
#     m = 0
#     if len(rel) < 5:
#         m = 0
#     else:
#         m = rel[0] * rel[1] * rel[2] * rel[3]* rel[4]
#     if 0<m<i:
#         j+=1
#         res.append([j,m])
# print(*res)
## [1, 3200] [2, 1728] [3, 21632] [4, 1260] [5, 1152]

#### 16
# for x in range(10):
#     for y in range(1000):
#         f = int("1" + str(x) + "954" + str(y) + "21")
#         if f % 3023 == 0:
#             print(f)
# for x in range(10):
#     f = int("1" + str(x) + "954" + "21")
#     if f % 3023 == 0:
#         print(f)
## 1895421
## 1295437121
## 1395498421
## 1795441321

#### 17
# for x in range(10):
#     for y in range(1000):
#         f = int("1" + str(x) + "2139" + str(y) + "4")
#         if f % 2023 == 0:
#             print(f, f // 2023)
# for x in range(10):
#     f = int("1" + str(x) + "2139" + "4")
#     if f % 2023 == 0:
#         print(f, f // 2023)

## 162139404 80148
## 1321399324 653188
## 1421396214 702618
## 1521393104 752048

#### 18
# def is_dels(n):
#     count = 0
#     for i in range(1, 1 + int(n ** 0.5)):
#         if n % i == 0:
#             if i == n // i:
#                 if i % 2 == 1:
#                     count += 1
#             else:
#                 if i % 2 == 1:
#                     count += 1
#                 if (n // i) % 2 == 1:
#                     count += 1
#         if count > 5:
#             return False
#     if count == 5:
#         return True
#     else:
#         return False
#
# res = []
# for i in range(45_000_000, 50_000_001):
#
#     if is_dels(i):
#         res.append(i)
#         print(res)
## не свезло
# povt = [3,5,2,6,3,8,8,8,9]
# print(povt.count(8))
class Solution(object):
    def runningSum(self, nums):
      return sum(nums)
    print(runningSum(1,[1,2,3,4]))