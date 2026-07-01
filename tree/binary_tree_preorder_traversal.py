"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Attempt 1: Using intuition and recursion


# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root:
#             return (
#                 [root.val]
#                 + self.preorderTraversal(root.left)
#                 + self.preorderTraversal(root.right)
#             )

#         return []


# Attempt 2: Cleaner version with less space?
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def traverse(root: Optional[TreeNode]):
#             if not root:
#                 return

#             result.append(root.val)
#             traverse(root.left)
#             traverse(root.right)

#         traverse(root)

#         return result


# Attempt 3: Using stack and iterations


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []

        curr = root

        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right

        return result
