"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""

from typing import Optional

# Attempt 1: Using extra space storing all the nodes?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head:
#             return

#         extra = []

#         temp = head
#         while temp:
#             extra.append(temp)
#             temp = temp.next

#         extra[len(extra) - n] = None
#         dummy = ListNode()
#         temp = dummy

#         for node in extra:
#             if node:
#                 temp.next = node
#                 temp = temp.next

#         temp.next = None
#         return dummy.next


# Attempt 2: Trying to optimise the problem


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

#         if head is None:
#             return

#         dummy = ListNode()

#         temp = dummy
#         slow = head  # tracking node to be removed
#         fast = head

#         while n:
#             fast = fast.next
#             n -= 1

#         while fast:
#             fast = fast.next
#             temp.next = slow

#             temp = temp.next
#             slow = slow.next

#         slow = slow.next
#         temp.next = slow
#         temp = temp.next

#         while slow:
#             slow = slow.next
#             temp.next = slow
#             temp = temp.next

#         return dummy.next


# Attempt 3: Clean solution without rebuilding the whole list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
