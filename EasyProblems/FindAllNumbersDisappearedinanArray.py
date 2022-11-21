# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


def findDisappearedNumbers(nums):
    num = set(nums)
    new_nums = []
    for i in range(1, len(nums) + 1):
        if i not in num:
            new_nums.append(i)
    return new_nums


a = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(a))

