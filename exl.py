file = open("X:\\Github\\ready\\9-1.csv")
for i in file:
    print(i.rstrip().split(";"))
file.close()
