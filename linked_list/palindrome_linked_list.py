"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional

# Attempt 1: Using extra storage


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        nodes = []
        temp = head

        while temp:
            nodes.append(temp.val)
            temp = temp.next

        l, r = 0, len(nodes) - 1

        while l < r:
            if nodes[l] != nodes[r]:
                return False

            l += 1
            r -= 1

        return True


# Attempt 2: Using fast / slow, reverse pattern


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            slow = slow.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev

            prev = slow
            slow = temp

        while head and prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next

        return True
