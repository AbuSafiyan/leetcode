# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number


def thirdMax(nums):
    nums = sorted(list(set(nums)))
    if len(nums) > 2:
        print(nums[-3])
    print(nums[-1])


a = [3, 2]
thirdMax(a)
