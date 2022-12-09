# Given an integer array nums, move all the even integers at the beginning of the array followed by all the
# odd integers. Return any array that satisfies this condition.
# Example:
# Input: nums = [3, 1, 2, 4]
# Output: [2, 4, 3, 1]
# Explanation: The outputs[4, 2, 3, 1], [2, 4, 1, 3], and [4, 2, 1, 3] would also be accepted.

def sortArrayByParity(nums):
    nums.sort()
    l1 = []
    l2 = []
    for i in nums:
        if i%2!=0:
            l1 = l1 + [i]
        else:
            l2 = l2 + [i]
    return l2+l1



a = [3, 1, 2, 4]
print(sortArrayByParity(a))
