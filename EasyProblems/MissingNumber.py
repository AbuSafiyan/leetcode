def missingNumber(nums):
    num = len(nums)
    su = sum(nums)
    num1 = (num * (num + 1)) // 2 - su
    return num1


a = [0, 1, 3, 4]
print(missingNumber(a))
