import itertools
# n = itertools.count(7,14)
# for i in range(757457):
#     print(next(n))
# c1=itertools.count(5,10)
# print(next(c1))#Output:5
# print(next(c1))#Output:10
# print(next(c1))#Output:15
import itertools
l1=[1,2,3]
#using list iterable as an argument in itertools.cycle()
l2=itertools.cycle(l1)
print (l2)#Output:<itertools.cycle object at 0x02F794E8>

count=0
for i in l2:
    #It will end in infinite loop. So have to define terminating condition.
    if count > 15:
        break
    else:
        print (i,end=" ")#Output:1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1
        count+=1