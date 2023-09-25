def matrix_addition(a, b):
    if len(a) == 1:
        return [a[0] + b[0]]
    else:
        for i in range(len(a)):
            for j in range(len(a[i])):
                a[i][j] += b[i][j]
        return a


print(f"1: \n {matrix_addition([1], [1])}")
print(f"2: \n{matrix_addition([[1, 2], [1, 2]], [[2, 3], [2, 3]]) }")
print(f"3: \n {matrix_addition([[1]], [[2]])}")