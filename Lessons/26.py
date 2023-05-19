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
# def main():
#     with open("X:\\Github\\some_files\\26\\2.txt") as file:
#         docs = file.readline()
#         array = [int(i) for i in file]
#     count_cargo, m_weight = list(map(int, docs.split()))
#     primary_weight = []
#     ind_ar = []
#     for i in range(len(array)):
#         if 200 <= array[i] <= 210:
#             primary_weight.append(array[i])
#             ind_ar.append(i)
#     primary_weights = sum(primary_weight)
#     m_weight = m_weight - primary_weights
#     for i in sorted(ind_ar, reverse=True):
#         array.pop(i)
#     array = sorted(array)
#     fill_cargo = 0
#     res = 0
#     startl = 0
#     for i in range(len(array)):
#         if fill_cargo <= m_weight and (fill_cargo + array[i] < m_weight):
#             fill_cargo += array[i]
#         else:
#             fill_cargo -= array[i]
#             startl = i
#             break
#     for i in range(startl, len(array)):
#         if array[i] + fill_cargo <= m_weight:
#             continue
#         else:
#             res = array[i - 1]
#             break
# 
#     print(startl, res)
# 110 161

if __name__ == "__main__":
    main()
