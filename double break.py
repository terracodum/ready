numb = []
def solution(number):
    for i in range(1,number):
        if (i % 3)==0 and (i%5)== 0:
            numb.append(i)
        elif i%3 ==0:
            numb.append(i)
        elif i%5 ==0:
            numb.append(i)
            print(numb)
    num_sum = sum(numb)
    return num_sum
print(solution(16))