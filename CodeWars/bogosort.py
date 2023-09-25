import random
def bogo_sort(n):

    list = list(n)
    while list != sorted(list):
        random.shuffle(list)
    return list
print(bogo_sort("4, 6, 1, 67, 23, 7, 8, 3"))