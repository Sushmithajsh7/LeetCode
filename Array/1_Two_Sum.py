from typing import List
import unittest
import unittest.main

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            second = target - nums[i]

            if second in d:
                return [d[second],i]
            d[nums[i]] = i


class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution.twoSum(nums = [2,7,11,15], target = 9), [0,1])
    def test_2(self):
        self.assertEqual(Solution.twoSum(nums = [3,2,4], target = 6), [1,2])
    def test_3(self):
        self.assertEqual(Solution.twoSum(nums = [3,3], target = 6), [0,1])

if __name__ == '__main__':
    unittest.main()