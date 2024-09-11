import unittest
import unittest.main

class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        i=j=0
        while i<len(s) and j< len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            # print(i,j)
        return i == len(s)
    
class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution.isSubsequence(s = "abc", t = "ahbgdc"), True)
    def test_2(self):
        self.assertEqual(Solution.isSubsequence(s = "axc", t = "ahbgdc"), False)

if __name__ == '__main__':
    unittest.main()
        