"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Attempt 1: Using intuition
# this solution fails
#class Solution:
 #   def inorderTraversal(self, node: Optional[TreeNode]):
  #      result = []
#
 #       def traversal(node: Optional[TreeNode]) -> None:
  #          if not node:
   #             return
#
 #           traversal(node.left)
  #          result.append(node.val)
   #         traversal(node.right)

    #    traversal(node)
     #   return result

    #def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
     #   p_structure = self.inorderTraversal(p)
      #  q_structure = self.inorderTraversal(q)
       # return p_structure == q_structure


class Solution:
    def isSameTree(self,p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False

        return p.val == q.vall and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
