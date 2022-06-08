def containsNearbyDuplicate(nums, k):
    if len(set(nums)) == len(nums):
        return False

    for i in range(len(nums)):
        for j in range(i, len(nums)):

            if nums[i] == nums[j]:
                if abs(i - j) <= k:
                    return True
    return False


s = [1, 2, 3, 1, 2, 3]
print(containsNearbyDuplicate(s, 2))
