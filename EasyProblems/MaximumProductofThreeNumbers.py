# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
# Example
# Input: nums = [1, 2, 3]
# Output: 6


def maximumProduct(nums):
    nums.sort()
    mul1 = nums[-1] * nums[-2] * nums[-3]
    mul2 = nums[0] * nums[1] * nums[-1]
    print(mul1)
    print(mul2)
    return max(mul1, mul2)


a = [-100, -98, -1, 2, 3, 4]
print(maximumProduct(a))