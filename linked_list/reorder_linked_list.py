"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

from typing import Optional

# Attemp 1: Using intuition


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         from collections import deque

#         if not head:
#             return

#         temp = head
#         elements = deque()

#         while temp:
#             if temp != head:
#                 elements.append(temp)

#             temp = temp.next

#         temp = head
#         while elements:
#             temp.next = elements.pop()
#             temp = temp.next

#             if not elements:
#                 break

#             temp.next = elements.popleft()
#             temp = temp.next

#         temp.next = None


# Attemp 2: Dividing the linked list through the middle and then reordering


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def divideList(
        self, head: Optional[ListNode]
    ) -> list[Optional[ListNode], Optional[ListNode]]:
        if not head or not head.next:
            return [None, None]

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next if slow.next else None
        slow.next = None

        return [head, right]

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next

            curr.next = prev
            prev = curr

            curr = temp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        left, right = self.divideList(head)
        reversedRight = self.reverseList(right)

        return reversedRight
