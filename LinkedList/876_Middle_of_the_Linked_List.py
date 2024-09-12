# Definition for singly-linked list.
from typing import Optional
import unittest
import unittest.main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
        s,f = head,head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
        
class TestClass(unittest.TestCase):
    def test_1(self):
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        e = ListNode(5)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = None
        self.assertEqual(Solution.middleNode(head=a).val, 3)
    def test_2(self):
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        e = ListNode(5)
        f = ListNode(6)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = None
        self.assertEqual(Solution.middleNode(head=a).val, 4)

if __name__ == '__main__':
    unittest.main()
    
    

        