"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Attempt 1: Using intuition
# Failed for time limit exceeded
#class Solution:
#    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#        if p is None and q is None: return True
#        if p is None or q is None: return False
#        
#        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#
#    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#        def searchNodes(root: Optional[TreeNode], val: int) -> list[TreeNode]:
#            result = []
#
#            def traverse(node):
#                if node is None:
#                    return
#
#                traverse(node.left)
#                if node.val == val: result.append(node)
#                traverse(node.right)
#
#            traverse(root)
#
#            return result
#
#        nodesToLook = searchNodes(root, subRoot.val)
#        if not nodesToLook: return False
#        
#        for node in nodesToLook:
#            if self.isSameTree(node, subRoot): return True 
#
#        return False

# Attempt 2: Combining search and comparison

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True 

        if root is None:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)      
