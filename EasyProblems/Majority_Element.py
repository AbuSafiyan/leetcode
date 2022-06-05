def majorityElement(nums):
    m = 0
    i = 0
    for num in range(len(nums)):
        if i == 0:
            m = nums[num]
            i = 1
        elif m == nums[num]:
            i += 1
        else:
            i -= 1
    return m


s = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(s))
