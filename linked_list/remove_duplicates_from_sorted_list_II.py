"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Attempt 1: Using intuition
# Failed with this solution
#class Solution:
#    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        if head is None: return head
#
#        last_same = head
#        while last_same and last_same.next:
#            if last_same.val == last_same.next.val:
#                last_same = last_same.next
#            else:
#                break
#
#        temp = None
#        if last_same != head:   
#            temp = last_same
#            last_same.next = None
#
#        head = temp if temp else head
#        head.next = self.deleteDuplicates(head.next)
#    
#        return head

# Attempt 2: Using a hashmap 
#class Solution:
#    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        bucket = {}
#        while head:
#            if head is None:
#                break
#            bucket[head.val] = bucket.get(head.val, 0) + 1
#            head = head.next
#        
#        newHead = ListNode()
#        temp = newHead
#        for h, f in bucket.items():
#            if f == 1:
#                temp.next = ListNode(h)
#                temp = temp.next
#        
#        return newHead.next
                
# Attempt 3: Using iteration             
# Incomplete
#class Solution:
#    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        dummy = ListNode()
#        prev = dummy
#        curr = head
#        
#        last_same = curr
#        while curr and curr.next:
#            if curr.val == curr.next.val:
#                curr = curr.next
#            else: break
#       


