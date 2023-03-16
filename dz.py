long = []
for i in range(101,1000):
    string ="1"*i
    while "111" in string:
        string = string.replace("111", "22", 1)
        string = string.replace("222", "11", 1)
    if string.count("1")==1:
        long.append(i)
print(min(long))