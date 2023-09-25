# num = 16

def dels(num):
    array = []
    for i in range(1,int(num**0.5)+1):
        if num % i ==0 :
            array.append(i)
            array.append(num//i)
    array = sorted(list(set((array))))
    return array
# print(array)
# def is_simple(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True
# counter = 0
# for i in range(245690,245757):
#     counter+=1
#     if is_simple(i):
#         print(counter,i)


for i in range(185311,185331):
    arrays = dels(i)
    if len(arrays)==4:
        print(*arrays)