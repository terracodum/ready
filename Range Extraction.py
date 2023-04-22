def solution(args):
    result = ""
    current = []
    print(args)
    args.append(args[-1] - 2)
    print(args)
    for i in range(len(args) - 1):
        if abs(args[i] - args[i + 1]) == 1:
            current.append(args[i])
        else:
            current.append(args[i])
            result += str(current[0])
            if len(current) > 2:
                result += "-" + str(current[-1])
            elif len(current) == 2:
                result += "," + str(current[-1])
            result += ","
            current = []
    return result.rstrip(",")


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# '-6,-3-1,3-5,7-11,14,15,17-20'