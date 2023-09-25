# with open("C:\\Users\\nikit\\Downloads\\27-B_demo.txt") as file:
#     serv = file.readline()
#     array = [list(map(int,(i.split()))) for i in file]
#
# arsd =[]
# for  i in range(len(array)):
#     let = abs(array[i][0] - array[i][1])
#     if let != 0  and let %3 != 0:
#         arsd.append(let)
# print(array)
# summ= 0
# for i in range(len(array)):
#     summ += max(array[i])
# if summ % 3 !=0:
#     print(summ)
# else:
#     ras = min(arsd)
#     summ -= ras
#     print(ras)
#     if summ % 3 !=0:
#         print(summ)
####################
# with open("C:\\Users\\nikit\\Downloads\\27990_B.txt") as file:
#     serv = file.readline()
#     array = [int(i) for i in file]
# print(len(array))
#
# count_31 = count_2 = count_62 = count_sq = 0
# for i in range(len(array)):
#     if array[i] % 62 == 0:
#         count_62 += 1
# for i in range(len(array)):
#     if array[i] % 31 == 0 and array[i] % 62 != 0:
#         count_31 += 1
#     elif array[i] % 2 == 0 and array[i] % 62 != 0:
#         count_2 += 1
#
# first = (len(array) - count_62) * count_62
# second = count_31 * count_2
# third = (count_62 * (count_62 - 1)) / 2
# print(first + second + third)
# counter = 0
# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if (array[i]*array[j])%62 == 0:
#             counter+=1
# print(counter)
with open("X:\\Github\\some_files\\275\\4B.txt") as file:
    serv = int(file.readline())
    array = [int(i) for i in file]

rsr = list(filter(lambda x: x % 17 == 0, array))
rsr = sorted(rsr)
array = sorted(array, reverse=True)
array.remove(rsr[-1])
print(rsr[-1])
print(array)
for i in range(len(array)):
    max_sum = rsr[-1] + array[i]
    if max_sum % 2 == 0:
        print(rsr[-1], array[i])
        break
