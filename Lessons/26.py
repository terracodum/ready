# with open("C:\\Users\\nikit\\Downloads\\27881.txt") as file:
#     serv = file.readline()
#     array = [int(i) for i in file]
# array = sorted(array)
# # storage =
# # people =
# startn = 0
# storage, people = list(map(int, serv.split()))
# print(storage, people)
# fill_store = 0
# for i in range(len(array)):
#     if fill_store<=storage and (array[i] + fill_store < storage):
#         fill_store += array[i]
#     else:
#         print(i,fill_store)
#         startn = i
#         fill_store -= array[i-1]
#
#         break
# maxn = 0
# for j in range(startn,len(array)):
#     if fill_store + array[j] <=storage:
#         continue
#     else:
#         maxn = array[j-1]
#         print(maxn)
#         break
# print(startn, maxn)
#######################################################
##  1
# with open("X:\\Github\\some_files\\26\\1.txt") as file:
#     serv = file.readline()
#     array = [int(i) for i in file ]
# startl = 0
# storage, people = list(map(int,serv.split()))
# array = sorted(array)
# fill_store = 0
# res = 0
# for i in range(len(array)):
#     if (array[i]+ fill_store <= storage) and fill_store <= storage:
#         fill_store += array[i]
#     else:
#         startl = i
#         fill_store -= array[i]
#         break
# for j in range(startl,len(array)):
#     if fill_store + array[j] <= storage:
#         continue
#     else :
#         res = array[j-1]
#         break
# print(startl, res)
# 568 50
### 2
# with open("X:\\Github\\some_files\\26\\6.txt") as file:
#     docs = file.readline()
#     array = [int(i) for i in file]
# count_cargo, m_weight = list(map(int, docs.split()))
# primary_weight = []
# ind_ar = []
# for i in range(len(array)):
#     if 200 <= array[i] <= 210:
#         primary_weight.append(array[i])
#         ind_ar.append(i)
# i_count = len(primary_weight)
# primary_weights = sum(primary_weight)
# m_weight = m_weight - primary_weights
# for i in sorted(ind_ar, reverse=True):
#     array.pop(i)
# array = sorted(array)
# fill_cargo = 0
# res = 0
# startl = 0
# print(array)
# print(m_weight)
# max_wei = []
# for i in range(len(array)):
#     if fill_cargo <= m_weight and (fill_cargo + array[i] < m_weight):
#         fill_cargo += array[i]
#         print(fill_cargo)
#         max_wei.append(array[i])
#     else:
#         startl = i
#         break
# print(max_wei)
# fill_cargo= fill_cargo- array[startl-1]
# count = startl + i_count
# # for i in range(startl, len(array)):
# #     if array[i] + fill_cargo <= m_weight:
# #         continue
# #     else:
# #         res = fill_cargo + array[i-1]
# #         break
# for i in range(len(max_wei)):
#     for j in range(i+1,len(array)):
#         max_weis = sum(max_wei) - max_wei[i]
#         if max_weis + array[j] > m_weight and array[j] not in max_wei:
#
#
#
#
#
# res = res + primary_weights
# print(count, res)
# 110 161
## 3
# def main():
#     import operator
#
#     with open("X:\\Github\\some_files\\26\\3.txt") as file:
#         serv = file.readline()
#         array = [i.rstrip() for i in file]
#     part, summ = list(map(int, serv.split()))
#     a_part = []
#     b_part = []
#
#     for i in range(len(array)):
#         if array[i][-1] == "A":
#             a_part.append(list(map(int, (array[i][:-2:]).split())))
#
#         else:
#             b_part.append(list(map(int, (array[i][:-2:]).split())))
#     sum_A = 0
#
#     for i in range(len(a_part)):
#         sum_A += a_part[i][0] * a_part[i][1]
#     summ = summ - sum_A
#     sum_B = 0
#     fill_stor = 0
#     b_part.sort(key=operator.itemgetter(0))
#     counter = 0
#     for i in range(len(b_part)):
#         while summ > b_part[i][0] and b_part[i][1] != 0:
#             summ = summ - b_part[i][0]
#             b_part[i][1] -= 1
#             counter+=1
#     return (counter,summ)
# if __name__ == "__main__":
#     print(main())
# for i in range(len(b_part)):
#     if fill_stor <= summ and fill_stor + b_par[i] <= summ:
#         fill_stor += b_par[i]
#     else:
#         last = i - 1
#         ost = summ - fill_stor
#         break
# for i in range(len(b_part)):
# print(last, ost)
# 164 3708
## 4
# with open("X:\\Github\\some_files\\26\\4.txt") as file:
#     num = int(file.readline())
#     array = [int(i) for i in file]
#
# counter = 0
# max_summ = 0
# for i in range(len(array)):
#     for j in range(i+1,len((array))):
#         if ((array[i] % 2 ==0) and (array[j] % 2 != 0)) or (array[j] % 2 ==0) and (array[i] % 2 != 0):
#             summ = array[i] + array[j]
#             print(i)
#             if summ in array:
#                 counter += 1
#                 max_summ = max(max_summ,summ)
# print(counter,max_summ)
######
# with open("X:\\Github\\some_files\\26\\5.txt") as file:
#     serv  =  file.readline()
#     array = [int(i.rstrip()) for i in file]
# m_weight, coll = list(map(int,serv.split()))
# array = sorted(array)
# fill_store = 0
# stert = 0
# last =0
# for i in range(len(array)):
#     if fill_store <= m_weight and fill_store + array[i] <= m_weight:
#         fill_store+=array[i]
#     else:
#         fill_store -= array[i-1]
#         ser = fill_store
#         stert = i
#         break
# print(stert)
# print(len(array))
# print(ser)
# print(m_weight)
# for i in range(stert,len(array)):
#     if ser + array[i] <= m_weight:
#         last = array[i]
#     else:
#         last = array[i-1]
# print(stert,last)
## 1612 90
#################### 25.05.23 ###########
# ## 1
# with open("X:\\Github\\some_files\\26_1\\1.txt") as file:
#     serv = file.readline()
#     array = [int(i) for i in file]
# array =sorted(array,reverse=True)
# pop_set =[]
# count = []
# counter =1
# last_ar = []
# while len(array)>0:
#     counter = 1
#     start = array[0]
#     array.pop(0)
#     for i in range(len(array)):
#         if start - array[i] >=5:
#             start = array[i]
#             pop_set.append(i)
#             counter+=1
#     print(pop_set,len(array))
#     pop_set = sorted(pop_set,reverse=True)
#     for j in pop_set:
#         array.pop(j)
#     pop_set.clear()
#     count.append(counter)
# print(len(count),max(count))
##
# import operator
#
# with open("X:\\Github\\some_files\\26_1\\2.txt") as file:
#     serv = file.readline()
#     array = [list(map(int, (i.split()))) for i in file]
# array.sort(key=operator.itemgetter(0))
# min_place = []
# take_array = []
# for i in range(len(array)):
#     take_array.clear()
#     tap = array[i][0]
#     for j in range(len((array))):
#         if array[j][0] == tap:
#             take_array.append(array[j])
#     take_array.sort(key=operator.itemgetter(1))
#     for k in range(len(take_array) - 1):
#         if take_array[k + 1][1] - take_array[k][1] == 14:
#             if take_array[-1][1] > take_array[k + 1][1] and take_array[0][1] < take_array[k][1]:
#                 min_place.append(take_array[k])
# min_place.sort(key=operator.itemgetter(0))
# print(min_place)
# lines = min_place[-1][0]
# res = min_place[-1][1] + 1
# print(lines, res)

# for k in range(len(array)):
#     counter =0
#     start = array[0]
#     pop_set.append(start)
#     for i in range(len(array)):
#         if array[i] - start >=5:
#             pop_set.append(i)
#             start = array[i]
#             counter +=1
#             print(i)
#
#         else:
#             last_ar.append(array[i])
#     count.append(counter)
#     pop_set = sorted(pop_set,reverse=True)
#     pop_set.remove(50)
#     # print(pop_set,len(array))
#     for j in pop_set:
#         array.pop(j)
#     pop_set.clear()
# print(count,last_ar)
# ##1766
#### 3
with open("X:\\Github\\some_files\\26_1\\3.txt") as file:
    serv = int(file.readline())
    array = [int(i) for i in file]
even = []
odd = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        even.append(array[i])
    elif array[i] % 2 == 1:
        odd.append(array[i])
max_sum = 0
counter = 0
lists = [odd, even]
for k in lists:
    for i in range(len(k)):
        for j in range(i + 1, len(k)):
            if (k[i] + k[j]) in even:
                counter += 1
                max_sum = max(max_sum, k[i] + k[j])
print(counter, max_sum)
## 10 933100556

#### 4
# with open("X:\\Github\\some_files\\26_1\\4.txt") as file:
#     serv = int(file.readline())
#     array = [int(i) for i in file]
# array.sort()
# sell_array = [i for i in array if i > 50]
# # bill = len(sell_array)
# low_array = [i for i in array if i <= 50]
# high_array = sell_array[int((len(sell_array))/2)::]
# sell_array = sell_array[:int((len(sell_array))/2):]
# bill = sum(low_array) + round((sum(sell_array))*0.75) + sum(high_array)
# print(sell_array[-1])
# print(bill)
## 469784 511
