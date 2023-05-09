import math
def sqr(sq):
    numb = math.isqrt(sq)
    numb = round(numb)
    numb = numb*numb
    if numb == sq:
        return True
    else:
        return False
def find_next_square(sq):
    if sqr(sq):
        num = math.isqrt(sq)
        num = num+1
        return num*num
    else:
        return -1
