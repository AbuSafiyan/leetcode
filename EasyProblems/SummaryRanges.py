def summaryRanges(nums):
    start_index = 0
    result = []
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            continue
        if start_index == i:
            result.append(str(nums[start_index]))
        else:
            result.append(str(nums[start_index]) + "->" + str(nums[i]))
        start_index = i + 1
    return result


a = [1, 2, 3, 4, 5, 20, 40]
print(summaryRanges(a))
