def missingNumber(nums):
    '''num = len(nums)
    su = sum(nums)
    num1 = (num * (num + 1)) // 2 - su
    return num1'''
    n = len(nums)
    res = n * (n + 1) // 2 - sum(nums)
    return res


a = [0, 1]
print(missingNumber(a))
