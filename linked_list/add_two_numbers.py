"""
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:

Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""

from typing import Optional

# Attempt 1: Using way extra space O(l1d + l2d + n) = O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         from collections import deque

#         l1d = deque()
#         l2d = deque()
#         n = deque()
#         temp = dummy = ListNode()

#         while l1:
#             l1d.appendleft(l1.val)
#             l1 = l1.next

#         while l2:
#             l2d.appendleft(l2.val)
#             l2 = l2.next

#         carry = 0

#         while l1d and l2d:
#             sum = carry + l1d.pop() + l2d.pop()
#             n.appendleft(sum % 10)
#             carry = sum // 10

#         while l1d:
#             sum = carry + l1d.pop()
#             n.appendleft(sum % 10)
#             carry = sum // 10

#         while l2d:
#             sum = carry + l2d.pop()
#             n.appendleft(sum % 10)
#             carry = sum // 10

#         print(carry)

#         while carry:
#             n.appendleft(carry)
#             carry = carry // 10

#         while n:
#             new_node = ListNode(n.pop())
#             temp.next = new_node
#             temp = temp.next

#         return dummy.next


# Attempt 2: Trying to use O(1) space


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        newHead = l1
        prev = None

        # Weaving the list into l1 btw
        while l1 and l2:
            s = carry + l1.val + l2.val

            l1.val = s % 10
            carry = s // 10

            prev = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = carry + l1.val
            l1.val = s % 10
            carry = s // 10

            prev = l1
            l1 = l1.next

        while l2:
            s = carry + l2.val
            l1 = ListNode(s % 10)
            carry = s // 10

            prev.next = l1
            prev = prev.next
            l2 = l2.next

        while carry:
            l1 = ListNode(carry % 10)
            prev.next = l1
            prev = prev.next
            carry //= 10

        return newHead
