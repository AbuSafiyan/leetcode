def singleNumber(nums):
    for num in nums:
        if not nums.count(num) > 1:
            return num


def singleNumberII(nums):
    newnum = set(nums)
    setsum = sum(newnum)
    numssum = sum(nums)
    lastsetsum = 2 * setsum

    result = lastsetsum - numssum
    return result


def singleNumberIII(nums):
    return 2 * sum(set(nums)) - sum(nums)


s = [2, 1, 2, 5, 1]
print(singleNumber(s))
