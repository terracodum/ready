file = open("X:\Github\\some_files\\10.csv")
counter = 0
for i in file:
    lets = i.rstrip().split(";")
    lets = map(int,lets)
    lets = sorted(lets,)
    if lets[0] < lets[1]+lets[2]:
        counter+=1
num = set()
print(counter)
file.close()
