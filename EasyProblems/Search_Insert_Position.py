class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

        return l


n = [1, 3, 4, 5]
x = Solution()
print(x.searchInsert(n))
