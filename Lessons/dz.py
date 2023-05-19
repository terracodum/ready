# # rot = open("X:\\Github\\some_files\\1.txt")
# array = [int(i) for i in rot]
# print(array)
# rot.close()
# take = []
# counter = 0
# sum = 1000000000
# for j in range(len(array)):
#     if str(array[j])[-1]=="2":
#         take.append(array[j])
#         print(take)
#         mit = min(take)
#         sekmit = mit*mit
#         print(mit)
# for i in range(len(array)-1):
#     if int(str(array[i])[-1])+1 == int(str(array[i+1])[-1]) or int(str(array[i])[-1])-1 == int(str(array[i+1])[-1]):
#         if (array[i] %5==0 and array[i+1]%5!=0 ) or (array[i]%5!=0 and array[i+1]%5==0):
#             if array[i]*array[i] + array[i+1]*array[i+1] > sekmit:
#                 counter +=1
#                 amm = array[i] + array[i+1]
#                 if amm >=0:
#                     sum = min(sum,amm)
# print(counter,sum)
#                                       №2
# rot = open("X:\\Github\\some_files\\2.txt")
# array = [int(i) for i in rot]
# print(array)
# rot.close()
# summ = 0
# counter = 0
# countersum = 0
# for j in array:
#     if j%2 ==1:
#         summ +=j
#         countersum +=1
# mid = summ/countersum
# sat = -100000000000
# for i in range(len(array)-1):
#     if array[i] % 5 == 0 and array[i+1]< mid:
#         sat = max(sat ,array[i]+array[i+1])
#         counter+=1
#         continue
#     elif array[i+1] % 5 == 0 and array[i]< mid:
#         sat = max(sat ,array[i]+array[i+1])
#         counter+=1
# print(counter,sat)
#############################################################
# rot = open("X:\\Github\\some_files\\7.txt")
# array = [int(i) for i in rot]
# rot.close()
# krat = 1000000000000
# counter = 0
# sum = -111111111111111
# print(len(array))
# for k in range(len(array)):
#     if array[k]%21 ==0:
#         krat = min(krat,array[k])
# for i in range(len(array)-1):
#     if array[i]%krat==0 or array[i+1]%krat==0:
#         counter +=1
#         sum = max(sum, array[i]+array[i+1])
# print(counter,sum)
###############################################################
# rot = open("X:\\Github\\some_files\\9.txt")
# array = [int(i) for i in rot]
# rot.close()
# krat = 1000000000000
# counter = 0
# sum = -111111111111111
# print(len(array))
# for i in range(len(array)-1):
#     for j in range(i+1,len(array)):
#         if (array[i] - array[j]) % 45==0:
#             if array[i] % 18 ==0 or array[j]%18==0:
#                 counter+=1
#                 sum = max(sum, array[i] - array[j])
# print(counter,sum)
####################################################################
# rot = open("X:\\Github\\some_files\\10.txt")
# array = [int(i) for i in rot]
# rot.close()
# krat = 1000000000000
# counter = 0
# sum = -111111111111111
# print(len(array))
# for i in range(len(array)-1):
#     for j in range(i+1,len(array)):
#         if (array[i] + array[j]) % 60==0:
#             if array[i] % 40 ==0 or array[j]%40==0:
#                 counter+=1
#                 sum = max(sum, array[i] + array[j])
# print(counter,sum)
# ####################################################################
# rot = open("X:\\Github\\some_files\\11.txt")
# array = [int(i) for i in rot]
# rot.close()
# maxj = -11111111111
# summ =0
# counter =0
# for j in range(len(array)):
#     if str(array[j])[-1]=="3":
#         maxj = max(maxj,array[j])
# for i in range(len(array)-1):
#     if (str(array[i])[-1]=="3" and str(array[i+1])[-1]!="3") or (str(array[i+1])[-1]=="3" and str(array[i])[-1]!="3"):
#         if (array[i]*array[i])+(array[i+1]*array[i+1]) > maxj*maxj:
#             counter +=1
#             summ = max(summ,array[i]**2+array[i+1]**2)
# print(counter,summ)
# ##########################################################################
# rot = open("C:\\Users\\nikit\\Downloads\\176.txt")
# array = [int(i) for i in rot]
# rot.close()
# maxj = 11111111111
# summ =-100000000000000000000000
# counter =0
# for j in range(len(array)):
#     if str(array[j])[-1]=="6":
#         maxj = min(maxj,array[j])
# for i in range(len(array)-1):
#     if (str(array[i])[-1]=="6" and str(array[i+1])[-1]!="6") or (str(array[i+1])[-1]=="6" and str(array[i])[-1]!="6"):
#         if (array[i]*array[i])+(array[i+1]*array[i+1]) < maxj*maxj:
#             counter +=1
#             summ = max(summ,array[i]*array[i]+array[i+1]*array[i+1])
# print(counter,summ)
# ################################################
# array = []
# summ = 100000000000000
# for x in range(0,8):
#     for y in range(0,8):
#         num1 = int(str(x)+"01"+str(y)+"4",9)
#         num2 = int(str(x)+str(y)+"544",8)
#         if (num1 + num2)%89==0:
#             summ = min(summ, num1+num2)
# print(summ//89)
################################################################
# array = "0123456789ABCDE"
# for x in array:
#     num1 = int("123"+x+"5",15)
#     num2 = int("1"+x+"233",15)
#     if (num1 + num2)%14==0:
#         print((num1+num2)/14)
############################################## 06.04.23 #####################################
##  №1
# num = 7*(512**1912)+6*(64**1954)-5*(8**1991)-4*(8**1980)-2022
# num = str(oct(num))
# print(num.count("7"))
##  №2
# lit = "0123456789ABCDEFGHI"
# print(len(lit))
# for x in lit:
#     num1 = int("321" + x + "4",19)
#     num2 = int("498" + x + "9",19)
#     num = num1 + num2
#     if num%23==0:
#         print(num / 23)
##  №3
# lit = "0123456789ABCD"
# for x in lit:
#     N = int("8"+x+"542",14)
#     M = int("8" + x + "12"+x,14)
#     for A in range(1,10000):
#         if( M + A )% N==0:
#             print(A)
# ##  №4
# lar = "0123456789"
# for x in lar :
#     num1 = int(x+"A04",13)
#     num2 = int("1D"+x+"3",18)
#     if (num1+num2)%184==0:
#         print((num1+num2)/184)
##  №5
# lit = "0123456789A"
# for x in lit:
#     for y in lit:
#         num1 = int(x+"341"+y,11)
#         num2 = int("56"+x+"1"+y,19)
#         if (num1+num2)%305==0:
#             print((num1+num2)/305)
##  №6
# lit = "01234567"
# for x in lit:
#     for y in lit:
#         num1 = int(y+"04"+x+"5",11)
#         num2 = int("253"+x+y,8)
#         if (num1+num2)%117==0:
#             print((num1+num2)/117)
##  №7
# with open("X:\\Github\\some_files\\9,4\\7.txt") as file:
#     array = [int(i) for i in file]
# maxsumm= 0
# counter = 0
# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#
#         if (array[i]+array[j])%7==0:
#             counter +=1
#             summ = array[i]+array[j]
#             maxsumm=max(maxsumm,summ)
# print(counter,maxsumm)
##  №8
# with open("X:\\Github\\some_files\\9,4\\8.txt") as file:
#     array = [int(i) for i in file]
# counters = 0
# summm=0
# for j in array:
#     if j%2==0:
#         counters+=1
#         summm +=j
# sum4 = summm/counters
# maxsumm = 0
# counter = 0
# for i in range(len(array)-1):
#     if (array[i]%3==0 and array[i+1]<sum4) or (array[i]<sum4 and  array[i+1]%3==0):
#         counter +=1
#         summ = array[i]+array[i+1]
#         maxsumm = max(maxsumm,summ)
# print(counter,maxsumm)
##  №9
# with open("X:\\Github\\some_files\\9,4\\9.txt") as file:
#     array = [int(i) for i in file]
# counter =0
# maxsumm = 0
# for i in range(len(array) - 3):
#         ars = sorted([array[i],array[i+1],array[i+2]])
#         if ars[2]**2 < ((ars[1]**2)+(ars[0]**2)):
#             counter +=1
#             maxsumm = max(maxsumm,(ars[0]+ars[1]+ars[2]))
# print(counter,maxsumm)
##  №10
# with open("X:\\Github\\some_files\\9,4\\10.txt") as file:
#     array = [int(i) for i in file]
# counter =0
# maxsumm = 0
# for i in range(len(array) - 3):
#         ars = sorted([array[i],array[i+1],array[i+2]])
#         if ars[2]**2 == ((ars[1]**2)+(ars[0]**2)):
#             counter +=1
#             maxsumm = max(maxsumm,(ars[0]+ars[1]+ars[2]))
# print(counter,maxsumm)
##  №11
# with open("X:\\Github\\some_files\\9,4\\11.txt") as file:
#     array =[int(i) for i in file]
# counters = 0
# summm=0
# for j in array:
#     if j%2==0:
#         counters+=1
#         summm +=j
# sum4 = summm/counters
# maxsumm = 0
# counter = 0
# for i in range(len(array)-1):
#     if (array[i]%3==0 or array[i+1]%3==0) and (array[i]<sum4 or array[i+1]<sum4 ):
#         counter +=1
#         summ = array[i]+array[i+1]
#         maxsumm = max(maxsumm,summ)
# print(counter,maxsumm)
##  №12
# with open("X:\\Github\\some_files\\9,4\\12.txt") as file:
#     array =[int(i) for i in file]
# sum = []
# for j in array:
#     if j%21==0:
#         sum.append(j)
# counter = 0
# maxsum =0
# minel = min(sum)
# for i in range(len(array)-1):
#     if array[i]%minel==0 or array[i+1]%minel==0:
#         counter+=1
#         maxsum = max(maxsum,array[i]+array[i+1])
# print(counter,maxsum)
############################## 09.04.23#############################
##  №1
# with open("X:\\Github\\some_files\\10,4\\1.txt") as file:
#     array = file.read()
# diktr = {}
# for i in range(len(array)):
#     if array[i] =="E":
#         if array[i+1] in diktr:
#             diktr[array[i+1]] +=1
#         else:
#             diktr[array[i+1]] =1
# print(diktr)
# print(max(diktr.values()))
##  №2
# with open("X:\\Github\\some_files\\10,4\\2.txt") as file:
#     array = [i.rstrip() for i in file]
# counter = 0
# for i in array:
#     if i.count("A") > i.count("E"):
#         counter += 1
# print(counter)
##  №3
# with open("X:\\Github\\some_files\\10,4\\3.txt") as file:
#     array = file.read()
# sim = 1
# maxsim = 0
# for i in range(len(array)-1):
#     if array[i] == "L" and array[i+1]== "L":
#         sim +=1
#     else:
#         maxsim = max(maxsim,sim)
#         sim = 1
# print(maxsim)
##  №4
# with open("X:\\Github\\some_files\\10,4\\4.txt") as file:
#     array = file.read()
# counter = 0
# maxcount = 0
# if array[0] == "X":
#     counter =1
# for i in range(1, len(array)):
#     if (array[i] == "X" and array[i-1] == "Z") or (array[i] == "Y" and array[i-1] == "X") or (array[i] == "Z" and array[i-1] == "Y"):
#         counter +=1
#     elif array[i] == "X" and array[i-1] != 'Z':
#         maxcount = max(maxcount, counter)
#         counter = 1
#     else:
#         maxcount = max(maxcount,counter)
#         counter = 0
# print(maxcount)
##  №5
# with open("X:\\Github\\some_files\\10,4\\5.txt") as file:
#     array = [i.rstrip() for i in file]
# maxlongstr = 0
# for string in array:
#     if string.count("G")<25:
#         strset = set(string)
#         for letter in strset:
#             mins = string.find(letter)
#             maxs = string.rfind(letter)
#             long = maxs - mins
#             maxlongstr = max(maxlongstr,long)
# print(maxlongstr)
##  №6
# with open("X:\\Github\\some_files\\10,4\\6.txt") as file:
#     array = file.read()
# maxlong = 0
# array = array.replace("da","ad")
# array = array.split("ad")
# for i in range(len(array)):
#     print(len(array))
#     if i ==0:
#         long = len(array[i]) + 1
#     elif i == 392:
#         long = len(array[i]) + 1
#     else:
#         long = len(array[i]) + 2
#     maxlong = max(maxlong,long)
# print(maxlong)
##  №7
# with open("X:\\Github\\some_files\\10,4\\7.txt") as file:
#     array = file.read()
# maxlong = 0
# array = array.split("A")
# for i in range(len(array)-1):
#     long = len(array[i])+len(array[i+1])+1
#     maxlong = max(maxlong,long)
# print(maxlong)
####################################### 13.04.23 #####################
##  №1
# with open("X:\\Github\\some_files\\13,04\\1.txt") as file:
#     array = [int(i) for i in file]
# counter = 0
# sum4 = 0
# for i in range(len(array)):
#     if array[i] %2 ==0:
#         counter +=1
#         sum4 += array[i]
# sum4 = sum4/counter
# count = 0
# summ = 0
# for i in range(len(array)-1):
#     if (array[i]%3==0 or array[i+1]%3==0) and (array[i]<sum4 or array[i+1]<sum4):
#         count+=1
#         summ = max(summ, array[i] + array[i+1])
# print(count,summ)
##  №2
# with open("X:\\Github\\some_files\\13,04\\2.txt") as file:
#     array = [int(i) for i in file]
# counter =summ = 0
# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if array[i]*array[j] %34 !=0:
#             counter+=1
#             summ = max(summ,array[i]+array[j])
# print(counter,summ)
# #  №3
# with open("X:\\Github\\some_files\\13,04\\3.txt") as file:
#     array = file.read()
# sog = "CDF"
# glas = "AO"
# count = 0
# maxlen = 0
# i = 0
# while i <= len(array)-2:
#     if (array[i] in sog) and (array[i+1] in sog) and (array[i+2] in glas):
#         count +=1
#         i += 3
#     else :
#         i+=1
#         count=0
#     maxlen = max(maxlen, count)
# print(maxlen)
##  №4
# with open("C:\\Users\\nikit\\Downloads\\244.txt") as file:
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
##  №5
# with open("X:\\Github\\some_files\\13,04\\5.txt") as file:
#     array = file.read()
# count = 0
# maxlen = 0
# i = 0
# while i<=len(array)-1:
#     if (array[i]=='A' and array[i+1]=='B') or (array[i]=='C' and array[i+1]=='B'):
#         count+=1
#         i+=2
#     else:
#         count=0
#         i+=1
#     maxlen =max(maxlen,count)
# print(maxlen)
##  №6
# with open("X:\\Github\\some_files\\13,04\\6.txt") as file:
#     array = file.read()
# array = array.split("E")
# maxlen = 0
# for i in range(len(array)):
#     if array[i].count("A")>=3:
#         res = len(array[i])
#         maxlen = max(maxlen,res)
# print(maxlen)
##  №7
# with open("X:\\Github\\some_files\\13,04\\7.txt") as file:
#     array = file.read()
# array = array.replace("KL","LK")
# array = array.split("LK")
# maxlen =0
# for i in range(len(array)):
#     lens = len(array[i])+2
#     maxlen = max(maxlen,lens)
# print(maxlen)
## №8
# with open("X:\\Github\\some_files\\13,04\\8.txt") as file:
#     array = [i.rstrip() for i in file]
# maxstring = 0
# for string in array:
#     if string.count("A")<25:
#         for letters in set(string):
#             mins = string.find(letters)
#             maxs = string.rfind(letters)
#             long = maxs - mins
#             maxstring  = max(maxstring,long)
# print(maxstring)
##  №9
# with open("X:\\Github\\some_files\\13,04\\9.txt") as file:
#     array = [i.rstrip() for i in file]
# dictr = {}
# list = []
# for i in range(len(array)):
#     dictr.setdefault(i, array[i].count("G"))
# print(dictr)
# ming = 10000000000
# for i in dictr:
#     ming = min(ming,dictr[i])
# print(ming)
# for i in dictr:
#     if dictr[i] == ming:
#         list.append(i)
# mig = list[0]
# string = array[mig]
# letters = {}
# for i in range(len(string)):
#     if string[i] in letters:
#         letters[string[i]] +=1
#     else:
#         letters[string[i]] = 1
#     let = letters.values()
# print(let)
# print(letters.keys())
##  №10
# with open("X:\\Github\\some_files\\13,04\\10.txt") as file:
#     array = file.read()
# letters = {}
# for i in range(len(array)-1):
#     if array[i-1] == array[i+1]:
#         if array[i] in letters:
#             letters[array[i]] +=1
#         else:
#             letters[array[i]] = 1
#     let = letters.values()
# print(let)
# print(letters.keys())
##  №11
# with open("X:\\Github\\some_files\\13,04\\11.txt") as file:
#     array = file.read()
# counter = 0
# maxcount = 0
# if array[0] == "L":
#     counter = 1
# for i in range(len(array)):
#     if (array[i] == 'D' and array[i-1]=="L") or (array[i] == "R" and array[i-1]=="D") or (array[i] == "L" and array[i-1]=="R"):
#         counter+=1
#     elif array[i]=="L" and array[i-1]!="R":
#         maxcount = max(maxcount,counter)
#         counter=1
#     else:
#         maxcount = max(maxcount,counter)
#         counter = 0
# print(maxcount)
##  №12
# with open("X:\\Github\\some_files\\13,04\\12.txt") as file:
#     array = file.read()
# les = ""
# for i in range(len(array)):
#     if array[i]=="E":
#         les = les.join(array[i+1])

############################################### 23.04.23 ################################################################
###  №1.1
# def game(first, step):
#     if first  >= 35 or step > 2:
#         return step == 2
#
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, step + 1), game(first+2, step + 1), game(first * 2, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, step + 1), game(first+2, step + 1), game(first * 2, step + 1)])
#
# for i in range(1, 35):
#     if game(i, 0):
#         print(i, end=" ")
###  №1.2
# def game(first, step):
#     if first  >= 35 or step > 3:
#         return step == 3
#
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, step + 1), game(first+2, step + 1), game(first * 2, step + 1)])
#     else:               # ход Пети
#         return all([game(first + 1, step + 1), game(first+2, step + 1), game(first * 2, step + 1)])
#
# for i in range(1, 35):
#     if game(i, 0):
#         print(i, end=" ")
# ###  №1.3
# def game(first, step):
#     if first  >= 35 or step > 4:
#         return step == 2 or step == 4
#
#     if step % 2 == 0:   # ход Вани
#         return all([game(first + 1, step + 1), game(first+2, step + 1), game(first * 2, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, step + 1), game(first+2, step + 1), game(first * 2, step + 1)])
#
# for i in range(1, 35):
#     if game(i, 0):
#         print(i, end=" ")
# ###  №2.1
# def game(first, second, step):
#     if first + second >= 82 or step > 2:
#         return step == 2
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first * 4, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*4, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first * 4, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*4, step + 1)])
#
# for i in range(1, 82):
#     if game(4, i, 0):
#         print(i, end=" ")
##  №2.2
# def game(first, second, step):
#     if first + second >= 82 or step > 3:
#         return step == 3
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first * 4, second, step + 1), game(first, second+1, step + 1), game(first, second*4, step + 1)])
#     else:               # ход Пети
#         return all([game(first + 1, second, step + 1), game(first * 4, second, step + 1), game(first, second+1, step + 1), game(first, second*4, step + 1)])
#
# for i in range(1, 82):
#     if game(4, i, 0):
#         print(i, end=" ")
###  №2.3
# def game(first, second, step):
#     if first + second >= 82 or step > 4:
#         return step == 2 or step == 4
#     if step % 2 == 0:   # ход Вани
#         return all([game(first + 1, second, step + 1), game(first * 4, second, step + 1), game(first, second+1, step + 1), game(first, second*4, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first * 4, second, step + 1), game(first, second+1, step + 1), game(first, second*4, step + 1)])
#
# for i in range(1, 82):
#     if game(4, i, 0):
#         print(i, end=" ")
###  №3.1
# def game(first, second, step):
#     if first + second >= 69 or step > 2:
#         return step == 2
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first * 2, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*3, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first * 2, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*3, step + 1)])
#
# for i in range(1, 59):
#     if game(10, i, 0):
#         print(i, end=" ")
###  №3.2
# def game(first, second, step):
#     if first + second >= 69 or step > 3:
#         return step == 3
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first * 2, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*3, step + 1)])
#     else:               # ход Пети
#         return all([game(first + 1, second, step + 1), game(first * 2, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*3, step + 1)])
#
# for i in range(1, 59):
#     if game(10, i, 0):
#         print(i, end=" ")
###  №3.3
# def game(first, second, step):
#     if first + second >= 69 or step > 4:
#         return step == 2 or step == 4
#     if step % 2 == 0:   # ход Вани
#         return all([game(first + 1, second, step + 1), game(first * 2, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*3, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first * 2, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second*3, step + 1)])
#
# for i in range(1, 59):
#     if game(10, i, 0):
#         print(i, end=" ")
###  №4.1
# def game(first, second, step):
#     if first + second <= 20 or step > 2:
#         return step == 2
#     if step % 2 == 0:   # ход Вани
#         return any([game(first - 1, second, step + 1), game(first // 2, second, step + 1), \
#                     game(first, second - 1, step + 1), game(first, second // 2, step + 1)])
#     else:               # ход Пети
#         return any([game(first - 1, second, step + 1), game(first // 2, second, step + 1), \
#                     game(first, second - 1, step + 1), game(first, second // 2, step + 1)])
#
# for i in range(11, 100):
#     if game(10, i, 0):
#         print(i, end=" ")
###  №4.2
# def game(first, second, step):
#     if first + second <= 20 or step > 3:
#         return step == 3
#     if step % 2 == 0:   # ход Вани
#         return any([game(first - 1, second, step + 1), game(first // 2, second, step + 1), \
#                     game(first, second - 1, step + 1), game(first, second // 2, step + 1)])
#     else:               # ход Пети
#         return all([game(first - 1, second, step + 1), game(first // 2, second, step + 1), \
#                     game(first, second - 1, step + 1), game(first, second // 2, step + 1)])
#
# for i in range(11, 100):
#     if game(10, i, 0):
#         print(i, end=" ")
###  №4.3
# def game(first, second, step):
#     if first + second <= 20 or step > 4:
#         return step == 4 or step == 2
#     if step % 2 == 0:   # ход Вани
#         return all([game(first - 1, second, step + 1), game(first // 2, second, step + 1), \
#                     game(first, second - 1, step + 1), game(first, second // 2, step + 1)])
#     else:               # ход Пети
#         return any([game(first - 1, second, step + 1), game(first // 2, second, step + 1), \
#                     game(first, second - 1, step + 1), game(first, second // 2, step + 1)])
#
# for i in range(11, 100):
#     if game(10, i, 0):
#         print(i, end=" ")
###  №5.1
# def game(first, second, step):
#     if first + second >= 75 or step > 2:
#         return step == 2
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first + second, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second+first, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first +second, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second+first, step + 1)])
#
# for i in range(1, 68):
#     if game(7, i, 0):
#         print(i, end=" ")
###  №5.2
# def game(first, second, step):
#     if first + second >= 75 or step > 3:
#         return step == 3
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first + second, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second+first, step + 1)])
#     else:               # ход Пети
#         return all([game(first + 1, second, step + 1), game(first +second, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second+first, step + 1)])
#
# for i in range(1, 68):
#     if game(7, i, 0):
#         print(i, end=" ")
###  №5.3
# def game(first, second, step):
#     if first + second >= 75 or step > 4:
#         return step == 2 or step ==4
#     if step % 2 == 0:   # ход Вани
#         return all([game(first + 1, second, step + 1), game(first + second, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second+first, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first +second, second, step + 1), \
#                     game(first, second+1, step + 1), game(first, second+first, step + 1)])
#
# for i in range(1, 68):
#     if game(7, i, 0):
#         print(i, end=" ")
###  №6.1
# def game(first, second, step):
#     if first + second >= 88 or step > 2:
#         return step == 2
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first * 3, second, step + 1), \
#                     game(first, second + 1, step + 1), game(first, second * 3, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first * 3, second, step + 1), \
#                     game(first, second + 1, step + 1), game(first, second * 3, step + 1)])
#
# for i in range(1, 71):
#     if game(6, i, 0):
#         print(i, end=" ")
###  №6.2
# def game(first, second, step):
#     if first + second >= 88 or step > 3:
#         return step == 3
#     if step % 2 == 0:   # ход Вани
#         return any([game(first + 1, second, step + 1), game(first * 3, second, step + 1), \
#                     game(first, second + 1, step + 1), game(first, second * 3, step + 1)])
#     else:               # ход Пети
#         return all([game(first + 1, second, step + 1), game(first * 3, second, step + 1), \
#                     game(first, second + 1, step + 1), game(first, second * 3, step + 1)])
#
# for i in range(1, 71):
#     if game(6, i, 0):
#         print(i, end=" ")
###  №6.3
# def game(first, second, step):
#     if first + second >= 88 or step > 4:
#         return step == 2 or step == 4
#     if step % 2 == 0:   # ход Вани
#         return all([game(first + 1, second, step + 1), game(first * 3, second, step + 1), \
#                     game(first, second + 1, step + 1), game(first, second * 3, step + 1)])
#     else:               # ход Пети
#         return any([game(first + 1, second, step + 1), game(first * 3, second, step + 1), \
#                     game(first, second + 1, step + 1), game(first, second * 3, step + 1)])
#
# for i in range(1, 71):
#     if game(6, i, 0):
#         print(i, end=" ")
################################################ 27.04.23 #################################################
### #1
# def de(m,n):
#     return m % n == 0
# for a in range(1,500):
#     flag = True
#     for x in range(1,500):
#         f = de(70,a) and (de(x,28) <= (de(x,a) or (not(de(x,21)))))
#
#         if f :
#             flag = True
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
#################################2
# def de(m,n):
#     return m % n == 0
# for a in range(1,500):
#     flag = True
#     for x in range(1,500):
#         f = ((not(de(72,x))) or(not(de(120,x)))) or (a-x>100)
#
#         if f :
#             pass
#         else:
#             flag = False
#             break
#     if flag:
#         print(a)
###############################3

# counter = 0
# for a in range(1,500):
#     flag = True
#     for x in range(1,500):
#         for y in range(1,500):
#             f = ((not(x<6)) or ((x**2)<a)) and (((not((y**2)<=a))) or (y<=6))
#
#             if f:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
#         counter +=1
# print(counter)
# ################################## 7
# for a in range(1,5000):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             f = ((y + 2*x) != 48) or (a<x) or (x<y)
#
#             if f == 1:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
#########################################9
# counter = 0
# for a in range(1,500):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             f = (not(x<a) or  (x**2 <81)) and (not(y**2 <= 36) or (y<=a))
#
#             if f == 1:
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag:
#         print(a)
#         counter+=1
# print(counter)
#####################################################11
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f  = (x&51 ==0) or ((not(x&41==0)) or (x&a == 0))
#         if f:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(a)
###################12
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f  = (not(x&105 ==0)) or ((not(x&58!=0)) or (x&a != 0))
#         if f:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(a)
#######################13
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f  = (x&a !=0)<=((x&10==0)<=(x&3!=0))
#         if f:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(a)
###############################14
# for a in range(500):
#     flag = True
#     for x in range(500):
#         f  = (x&17 ==0)<=((x&29!=0)<=(x&a!=0))
#         if f:
#             pass
#         else:
#             flag = False
#     if flag:
#         print(a)
#
########################### 5
####################################################################################
## 1
# with open("X:\\Github\\some_files\\adasf\\1.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
# counter = 0
# for i in range(len(array)):
#     array[i] = sorted(list(map(int,array[i])))
# print(array)
# for k in range(len(array)):
#     ars = array[k]
#     if (ars[0]**2) + (ars[1]**2) == ars[2]**2:
#         print(ars)
#         counter +=1
# print(counter)
## 2
# with open("X:\\Github\\some_files\\adasf\\2.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
# counter = 0
# for i in range(len(array)):
#     array[i] = sorted(list(map(int,array[i])))
# print(array)
# for i in range(len(array)):
#     ars = array[i]
#     if (ars[0] + ars[4])**2 > ars[1]**2 +ars[2]**2 + ars[3]**2:
#         counter+=1
# print(counter)
## 3
# with open("X:\\Github\\some_files\\adasf\\3.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
# counter = 0
# for i in range(len(array)):
#     array[i] = sorted(list(map(int,array[i])))
#
# for i in range(len(array)):
#     ars = array[i]
#     sum1 = ars[0] * ars[1] + ars[0]* ars[2]
#     sum2 = ars[1] * ars[2]
#     if ars[0] * ars[1] + ars[0]* ars[2] < ars[1] * ars[2]:
#         counter+=1
# print(counter)
## 4
# with open("X:\\Github\\some_files\\adasf\\4.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
# counter = 0
# for i in range(len(array)):
#     array[i] = sorted(list(map(int,array[i])))
# print(array)
# for i in range(len(array)):
#     if len(set(array[i])) == 5:
#         num = sum(array[i]) - sum(list(set(array[i])))
#         sr = (sum(list(set(array[i]))) - num)/4
#         if sr <= num*2:
#             counter+=1
# print(counter)
###########################
## 5
# with open("X:\\Github\\some_files\\adasf\\5.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
#     for j in range(len(array)):
#         array[j] = sorted(list(map(int,array[j])))
#     print(array)
# counter = 0
# for i in range(len(array)):
#     if len(set(array[i])) == 5:
#         if 3*(array[i][0]+array[i][-1]) <= 2*(array[i][1]+array[i][2]+array[i][3]):
#             counter+=1
# print(counter)
#  853
## 6
# with open("X:\\Github\\some_files\\adasf\\6.csv") as file:
#     array = [i.rstrip().split(";") for i in file]
#     for j in range(len(array)):
#         array[j] = sorted(list(map(int,array[j])))
#     print(array)
# counter = 0
# for i in range(len(array)):
#     if array[i][0] +array[i][1] > array[i][-1]:
#         counter += 1
# print(counter)
#  1842
## 7
# with open("X:\\Github\\some_files\\adasf\\7.txt") as file:
#     array = file.read()
# print(array)
# cog = "CDF"
# glas = "AO"
# counter = 0
# maxcount = 0
# i = 1
# while i != len(array)-1:
#     if (array[i] in cog) and (array[i-1] in cog) and (array[i+1] in glas):
#         i +=3
#         counter +=1
#         maxcount = max(maxcount,counter)
#     else :
#         i+=1
#         maxcount = max(maxcount, counter)
#         counter=0
#
# print(maxcount)
# 6
## 8
# import string
# sel = (string.ascii_uppercase)
# with open("X:\\Github\\some_files\\adasf\\8.txt") as file:
#     array = [i.rstrip() for i in file]
# mincount = 1000000000
# counter = 0
# maxstr = []
# for i in range(len(array)):
#     counter = array[i].count("N")
#     if counter < mincount:
#         mincount = counter
#         maxstr.clear()
#         maxstr.append(array[i])
#     elif counter == mincount:
#         maxstr.append(array[i])
#     if array[i].count("N") ==10:
#         print("succses")
# print(maxstr,mincount)
# dictr = {}
# for i in sel:
#     dictr.setdefault(i,maxstr[0].count(i))
# print(dictr)
# "Y"
## 9
# with open("X:\\Github\\some_files\\adasf\\9.txt") as file:
#     array = file.read
# print(array)
## 10
# with open("X:\\Github\\some_files\\adasf\\10.txt") as file:
#     array = [int(i) for i in file]
# print(array)
# count = []
# for i in range(len(array)):
#     if (array[i] // 100 == 0) and (array[i] // 10 > 0):
#         count.append(array[i])
# maxi = max(count)
# counter = 0
# maxsum = 0
# for i in range(len(array) - 1):
#     if ((9<array[i]<100) and (array[i + 1]<10 or array[i+1]>99) ) or ((9<array[i+1]<100) and (array[i]<10 or array[i]>99)):
#         if (array[i] + array[i + 1]) % maxi == 0:
#             counter +=1
#             maxsum = max(maxsum, array[i] + array[i + 1])
# print(counter,maxsum)
# # 23

