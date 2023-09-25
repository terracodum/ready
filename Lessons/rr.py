popt = open("C:\\Users\\nikit\\Downloads\\175.txt")
counter = 0
maxsum = -10000000
array = [int(i) for i in popt]
popt.close()
summ = 0
countersum = 0
for i in array:
    if i%2 ==1:
        summ +=i
        countersum+=1
mid = summ/countersum
for i in range(len(array)-1):
    if (array[i]%5==0 or array[i+1]%5==0) and (array[i]<mid or array[i+1]<mid):
        counter+=1
        maxsum = max(maxsum,array[i]+array[i+1])
print(counter, maxsum)