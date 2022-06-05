def contain_Duplicate(nums):
    d = set()
    for num in nums:
        if num in d:
            return True
        d.add(num)
    return False


s = [2, 14, 18, 22, 22]
print(contain_Duplicate(s))
