# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays, and you may
# return the result in any order.


def intersect(nums1, nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)
    return res


a = [4, 9, 5]
b = [9, 4, 9, 8, 4]
print(intersect(a, b))
