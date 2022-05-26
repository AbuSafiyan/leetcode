class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count


n = 101
a = Solution()
print(a.hammingWeight(n))
