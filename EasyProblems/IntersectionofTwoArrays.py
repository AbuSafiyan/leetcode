# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique, and you may return the result in any order.


def intersection(nums1, nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
    return list(set(res))


a = [1, 2, 2, 1]
b = [2, 2]
print(intersection(a, b))
