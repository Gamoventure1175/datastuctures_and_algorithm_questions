"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List

# Attempt 1: Using a dictionary with depth first search


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         levelMap = {}

#         def traverSalWithLevel(root: Optional[TreeNode], lvl=0):
#             if root is None:
#                 return

#             if lvl in levelMap:
#                 levelMap[lvl].append(root.val)
#             else:
#                 levelMap[lvl] = [root.val]

#             traverSalWithLevel(root.left, lvl + 1)
#             traverSalWithLevel(root.right, lvl + 1)

#         traverSalWithLevel(root)

#         result = []
#         for level in levelMap.values():
#             result.append(level)

#         return result


# Attempt 2: Using list with dfs


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: list[list[int]] = []

        def traverSalWithLevel(root: Optional[TreeNode], lvl=0):
            if root is None:
                return

            if lvl == len(result):
                result.append([root.val])
            else:
                result[lvl].append(root.val)

            traverSalWithLevel(root.left, lvl + 1)
            traverSalWithLevel(root.right, lvl + 1)

        traverSalWithLevel(root)
        return result
