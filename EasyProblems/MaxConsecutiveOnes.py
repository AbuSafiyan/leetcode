# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.


def findMaxConsecutiveOnes(nums):
    res = 0
    tmp = 0

    for num in nums:
        if num == 0:
            tmp = 0
        else:
            tmp += 1
            res = max(res, tmp)

    return res


a = [1, 1, 0, 0, 1, 0, 1, 1, 1, 1]
a.reverse()
print(findMaxConsecutiveOnes(a))
