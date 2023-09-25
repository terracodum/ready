def high_and_low(numbers):
    num_list = []
    while numbers.count(" ") != 0:
        indexsp = numbers.index(" ")
        num = numbers[:indexsp:]
        num_list.extend([num])
        numbers = numbers[indexsp + 1::]
    num_list.extend([numbers])
    num_list = list(map(int, num_list))
    num1 = str(max(num_list))
    num2 = str(min(num_list, default=0))
    return num1 + " " + num2


if __name__ == "__main__":
    print("fgfhd")
print(__name__)
