"""leetcode question 136"""
import unittest

class FindSingleNumber:

    def singleNumber(self, nums):
        for num in nums:
            if not nums.count(num) > 1:
                return num

    def singleNumberII(self, nums):
        new_num = set(nums)
        set_sum = sum(new_num)
        nums_sum = sum(nums)
        last_set_sum = 2 * set_sum

        result = last_set_sum - nums_sum
        return result

    def singleNumberIII(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


class test_cases(unittest.TestCase):

    find_single_number = FindSingleNumber()

    def test2(self):
        actual = [1, 2, 1, 5, 2]
        expected = 5
        self.assertEqual(self.find_single_number.singleNumber(actual), expected, "test case passed")

    def test1(self):
        actual = [2, 1, 2]
        expected = 1
        self.assertEqual(self.find_single_number.singleNumber(actual), expected, "test case passed")
