"""leetcode question 17"""


def singleNumber2(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num


s = [2, 1, 2, 5, 1, 2, 1]
print(singleNumber2(s))
