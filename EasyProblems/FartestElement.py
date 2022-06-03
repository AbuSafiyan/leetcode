import math


def  far(l):
    l.sort()
    least = l[0]
    max = l[-1]
    least = int(math.fabs(least))
    if least >= max:
        return l[0]
    else:
        return max


print(far([1,20,2,0,-100]))