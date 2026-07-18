"""
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:



Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:



Input: head = [1,2], index = -1

Output: false
Constraints:

0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.

"""

from typing import Optional

# Attempt 1: Using a cycle detection method published by some motherfucker


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#class Solution:
#    def hasCycle(self, head: Optional[ListNode]) -> bool:
#        if not head:
#            return False
#
#        fast = slow = head
#
#        while fast and slow:
#
#            if not fast.next:
#                return False
#            if not slow.next:
#                return False
#
#            fast = fast.next.next
#            slow = slow.next
#
#            if fast == slow:
#                return True
#
#        return False
    
# Much cleaner

    # def hasCycle(self, head):
    #     slow = fast = head

    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #         if slow is fast:
    #             return True

    #     return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: return False
        def traverse(p, q):
            if p and q is None:
                return False
            
            if p and q and p is q: return True

            if p.next and q.next is not None:
                return traverse(p.next, q.next.next)
            else:
                return False

        return traverse(head, head.next.next)
