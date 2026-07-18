"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
"""

from typing import Optional

# Attempt 1: Using intuition


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#class Solution:
#    def mergeTwoLists(
#        self, list1: Optional[ListNode], list2: Optional[ListNode]
#    ) -> Optional[ListNode]:
#        if not list1:
#            return list2
#
#        if not list2:
#            return list1
#
#        dummy = ListNode()
#        temp = dummy
#
#        while list1 and list2:
#            if list1.val <= list2.val:
#                dummy.next = list1
#                list1 = list1.next
#                dummy = dummy.next
#
#            else:
#                dummy.next = list2
#                list2 = list2.next
#                dummy = dummy.next
#
#        while list1:
#            dummy.next = list1
#            list1 = list1.next
#            dummy = dummy.next
#
#        while list2:
#            dummy.next = list2
#            list2 = list2.next
#            dummy = dummy.next
#
#        return temp.next

# Attempt 2: Using recursion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        def traversal(list1, list2):
            nonlocal head

            if list1 and list2:
                if list1.val <= list2.val:
                    head.next = list1
                    head = head.next
                    return traversal(list1.next, list2)

                head.next = list2
                head = head.next
                return traversal(list1, list2.next)
            
            elif list1 is None and list2:
                head.next = list2
                head = head.next
                return traversal(list1, list2.next)
            
            elif list2 is None and list1:
                head.next = list1
                head = head.next
                return traversal(list1.next, list2)
            
            return

        traversal(list1, list2)
        return temp.next
