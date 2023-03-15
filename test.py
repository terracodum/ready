numbers = "1 4 5 7"
num_list = []
while numbers.count(" ") != 0:
    indexsp = numbers.index(" ")
    num = numbers[:indexsp:]
    num_list.extend([num])
    numbers = numbers[indexsp + 1::]
num_list.extend([numbers])
print(num_list)
num_list = list(map(int, num_list))
print(num_list)
num1 = str(max(num_list))
print(num_list)
num2 = str(min(num_list , default= 0))
print(num1)
print(num2)
print(num_list)

print(num1 + " " + num2)

