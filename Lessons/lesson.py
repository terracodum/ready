# with open("X:\\Github\\some_files\\inf_22_10_20_24.txt") as file:
#     array = [i.rstrip() for i in file]
# counter = 0
# for i in array:
#     if i.count("E") > i.count("A"):
#         counter +=1
# print(counter)
################################
# with open("X:\\Github\\some_files\\zadanie24_21.txt", "r") as file:
#     array = file.read()
# maxsim = 0
# sim = 1
# # array = "FDORRRRGFDSRRRRFRGR"
# for i in range(len(array)-1):
#
#     if array[i]=="R" and array[i+1]=="R":
#         sim += 1
#     else:
#         maxsim = max(maxsim,sim)
#         sim = 1
# print(maxsim)
#######################
# with open("X:\\Github\\some_files\\zadanie24_22.txt", "r") as file:
#     array = file.read()
# maxsim =0
# cur = 1
# for i in range(len(array)-1):
#     if array[i] != array[i+1]:
#         cur+=1
#     else:
#         maxsim = max(maxsim,cur)
#         cur  = 1
# print(maxsim)
##################
# with open("X:\\Github\\some_files\\242.txt", "r") as file:
#     array = file.read()
# maxsim =0
# cur =1
# # array = "PQRSRTSGLGDPPPASDGPHGHJGPPPFGP"
# for i in range(len(array)-1):
#     if array[i] == array[i+1] == "P":
#         maxsim = max(maxsim,cur)
#         cur =1
#     else:
#         cur+=1
# print(maxsim)
##############################
# with open("X:\\Github\\some_files\\243.txt", "r") as file:
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
##################################### 27.04.23########################
