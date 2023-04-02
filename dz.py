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
