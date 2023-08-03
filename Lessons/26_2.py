import operator
with open("X:\\Github\\some_files\\вмспв\\1.txt") as file:
    count_sotr =int( file.readline())
    count_rooms = int(file.readline())
    array = [list(map(int,(i.split()))) for i in file]
print(count_rooms,count_sotr,array)
