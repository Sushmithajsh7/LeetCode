import unittest
import unittest.main
from typing import List

class Solution:

    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        # maxSoFar = 0
        # maxSum = min(nums)-1
    

        # for i in range(0, len(nums)):
          
        #     maxSoFar += nums[i]

        #     print(maxSoFar)
        #     print(maxSum)
        #     if maxSum < maxSoFar:
        #        maxSum = maxSoFar
        #     if maxSoFar < 0:
        #         maxSoFar = 0
            
        # return maxSum

        maxSum = nums[0]
        curMax = nums[0]

        for i in range(1,len(nums)):
            curMax = max(nums[i], curMax+nums[i])
            
            maxSum = max(curMax,maxSum)

        return maxSum



class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]), 6)
    def test_2(self):
        self.assertEqual(Solution.maxSubArray( nums = [1]), 1)
    def test_3(self):
        self.assertEqual(Solution.maxSubArray(nums = [5,4,-1,7,8]), 23)

if __name__ == '__main__':
    unittest.main()


        