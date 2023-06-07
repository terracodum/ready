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

with open("C:\\Users\\nikit\\Downloads\\27990_B.txt") as file:
    serv = file.readline()
    array = [int(i) for i in file]
print(array)
# counter = 0
# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if (array[i]*array[j])%62 == 0:
#             counter+=1
# print(counter)
for i in range(len(array)):
