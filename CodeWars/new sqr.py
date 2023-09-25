def solution(array_a, array_b):
    sum = 0
    for i in range(len(array_a)):
        sum += (array_a[i] - array_b[i])**2
    return sum/len(array_a)


a1 = [1, 2, 3]
a2 = [4, 5, 6]

print(solution(a1, a2)) # 9