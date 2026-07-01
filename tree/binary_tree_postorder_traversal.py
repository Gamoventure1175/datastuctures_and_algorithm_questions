"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

The number of the nodes in the tree is in the range [0, 100].
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


# Attempt 1: Using recursion
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def traversal(root: Optional[TreeNode]):
#             if not root:
#                 return

#             traversal(root.left)
#             traversal(root.right)
#             result.append(root.val)

#         traversal(root)
#         return result

# Attempt 2: Using iterations with stack


class Solution:
    def postorderTraversal(self, root):
        stack = []
        result = []

        curr = root
        last_visited = None

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]

            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                result.append(peek.val)
                last_visited = stack.pop()

        return result
