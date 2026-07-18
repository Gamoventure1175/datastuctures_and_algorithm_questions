"""

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""

# Using pointers to reverse the list in place

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Attempt 1: Using intuition
#class Solution:
#    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        prev = None
#        curr = head
#
#        if curr is None:
#            return
#
#        while curr is not None:
#            temp = curr.next
#            curr.next = prev
#
#            prev = curr
#            curr = temp
#
#        return prev


# Attempt 2: Using recurssion:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(left: Optional[ListNode], right: Optional[ListNode]):
            if left and right is None:
                return left
            
            if left is None and right is None:
                return None
            
            curr = right.next
            right.next = left
        
            return traverse(right, curr)
