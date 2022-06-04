"""leetcode question 136"""


def singleNumber(nums):
    for num in nums:
        if not nums.count(num) > 1:
            return num


def singleNumberII(nums):
    new_num = set(nums)
    set_sum = sum(new_num)
    nums_sum = sum(nums)
    last_set_sum = 2 * set_sum

    result = last_set_sum - nums_sum
    return result


def singleNumberIII(nums):
    return 2 * sum(set(nums)) - sum(nums)


s = [2, 1, 2, 5, 1]
print(singleNumber(s))
