def max_sequence(arr):
    maxsumm = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            summ = sum(arr[i:j:])
            maxsumm = max(maxsumm, summ)
    return maxsumm


print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))  # 6
