import unittest
import unittest.main

class Solution:

    """
    Uncomment whichever approach you want to test. Both approaches are similar. 
    But second approach uses dictionary or hash
    Aproach 1
    Time Complexity : 
    Space Complexity:
    
    Aproach 2
    Time Complexity : 
    Space Complexity:
    
    """
    @staticmethod
    def isValid(s: str) -> bool:
        ##############Approach 1
        # stack = []
        # for i in s:
        #     if i in ['(','[','{']:
        #         stack.append(i)
        #     else:
        #         if stack:
        #             popped_item = stack.pop()
        #             if popped_item == '(':
        #                 if i != ')':
        #                     return False
        #             elif popped_item == '[':
        #                 if i != ']':
        #                     return False
        #             elif popped_item == '{':
        #                 if i != '}':
        #                     return False
        #         else:
        #             return False
        # if stack :
        #     return False
        # return True


        #########Approach 2
        dict_paranthesis = {'(':')','{':'}','[':']'}
        stack = []

        for i in s:
            if i in dict_paranthesis:
                stack.append(i)
            elif not stack or dict_paranthesis[stack.pop()] != i :
                        return False
        
        return len(stack) == 0




class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution.isValid("()"), True)
    def test_2(self):
        self.assertEqual(Solution.isValid("()[]{}"), True)
    def test_3(self):
        self.assertEqual(Solution.isValid("(]"), False)
    def test_4(self):
        self.assertEqual(Solution.isValid("([])"), True)

if __name__ == '__main__':
    unittest.main()
    