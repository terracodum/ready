with open("X:\\Github\\some_files\\10,4\\6.txt") as file:
    array = file.read()
maxlong = 0
array = array.replace("da","ad")
array = array.split("ad")
for i in range(len(array)):
    print(len(array))
    if i ==0:
        long = len(array[i]) + 1
    elif i == 392:
        long = len(array[i]) + 1
    else:
        long = len(array[i]) + 2
    maxlong = max(maxlong,long)
print(maxlong)