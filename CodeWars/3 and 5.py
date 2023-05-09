numb = []
def solution(number):
    for i in range(1,number):
        if i%3 ==0:
            numb.append(i)
            print(numb)
            continue
        elif i%5 ==0:
            numb.append(i)
            print(numb)
            continue
    num_sum = sum(numb)
    return num_sum
