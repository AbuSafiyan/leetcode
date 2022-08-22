def moveZeros(nums):

    idx = 0
    for i in range(len(nums)):
        if nums[idx] == 0:
            nums.pop(idx)
            nums.append(0)
        else:
            idx += 1
    return nums


a = [0, 1, 0, 3, 13]
print(moveZeros(a))
