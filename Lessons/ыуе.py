popt = open("C:\\Users\\nikit\\Downloads\\175.txt")
# array = []
# for i in popt:
#     array.append(int(i))
# print(array, len(array))
counter = 0
maxsum = -10000000
array = [int(i) for i in popt]
popt.close()
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if (array[i] + array[j])%2==1 and (array[i] * array[j])%5==0:
            counter +=1
            maxsum = max(maxsum,array[i]+array[j])
print(counter,maxsum)
