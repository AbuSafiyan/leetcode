"""leetcode question 260"""


def singleNumber3(nums):
    ls = []

    for num in nums:
        if nums.count(num) == 1:
            ls.append(num)
    return tuple(ls)


s = [2, 1, 2, 5, 1, 4]
print(singleNumber3(s)