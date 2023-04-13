def ranges(args):
    # print(type(args))
    args = sorted(args)
    num1 = 10000000000000000000000000
    for i in range(len(args)-1):

        if args[i]+1 == args[i+1]:
            num1 = min(args[i],num1)
        else:
            num2 = args[i]
    res =str(num1)+"-"+ str(num2)
    return [res, args.index(num2)]

def solution(args):

    args = sorted(args)
    result = ""
    for i in range(len(args)-1):
        if args[i]+1 == args[i+1]:
            ran = (ranges(args))[0]
            print(type(args))
            result = result.join(ran)

            continue
        else:
            num2 = args[i]
    return result










print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# '-6,-3-1,3-5,7-11,14,15,17-20'