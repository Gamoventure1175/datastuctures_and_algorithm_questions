"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 

Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Attempt 1: Using intuition
#class Solution:
#    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:
#        if not list1:
#            return list2
#
#        if not list2:
#            return list1
#
#        newHead = ListNode()
#        temp = newHead
#
#        while list1 and list2:
#            if list1.val <= list2.val:
#                temp.next = list1
#                
#                list1 = list1.next
#                temp = temp.next
#            else:
#                temp.next = list2
#
#                list2 = list2.next
#                temp = temp.next
#
#        while list1:
#            temp.next = list1
#            list1 = list1.next
#            temp = temp.next
#
#        while list2:
#            temp.next = list2
#            list2= list2.next
#            temp = temp.next
#
#        return newHead.next
#
#    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#        newHead = None 
#
#        for l in lists:
#            newHead = self.mergeTwoLists(newHead, l)
#
#        return newHead
