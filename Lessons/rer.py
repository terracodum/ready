x = [5,7,3,6,8,0,3,4,7,9,0,2]
y = [9,6,3,6,8,3,6,8,4,5,7,4]
print(list(map(lambda s : 'a' if s%10 > 5 else 'b', [x[i]+y[i] for i in range(len(x))])))