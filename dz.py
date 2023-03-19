long = []
for i in range(201,1000):
    string ="1"*i
    while "1111" in string:
        string = string.replace("1111", "22", 1)
        string = string.replace("222", "1", 1)
    lat = string.count("1")
    long.append(lat)
    if string.count("1")==4:
        print(s)