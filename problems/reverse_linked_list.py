"""
Reverse Linked List
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

I am currently solving this problem.
"""

# Approach 1: Rewiring the backwards direction (Converting single link to double?)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoublyLinkedNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:

            next_node = curr.next


if __name__ == "__main__":
    solution = Solution()

    node = ListNode(1)

    for i in range(2, 11):
        node.next = ListNode(i)
        node = node.next
