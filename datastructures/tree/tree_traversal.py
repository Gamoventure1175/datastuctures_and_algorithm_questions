from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Types of traversal techniques


# 1. Pre-order traversal
def preorder_traveral(start: TreeNode, traversal):
    """Root -> Left -> Right"""

    if start:
        traversal += str(start.val) + " - "
        traversal = preorder_traveral(start.left, traversal)
        traversal = preorder_traveral(start.right, traversal)

    return traversal


# 2. In-order traversal
def inorder_traversal(start: TreeNode, traversal):
    """Left -> Root -> Right"""
    if start:
        traversal = inorder_traversal(start.left, traversal)
        traversal += str(start.val) + " - "
        traversal = inorder_traversal(start.right, traversal)

    return traversal


# 3. Post-order traversal
def postorder_traversal(start: TreeNode, traversal):
    """Left->Right->Root"""
    if start:
        traversal = postorder_traversal(start.left, traversal)
        traversal = postorder_traversal(start.right, traversal)
        traversal += str(start.val) + " - "
    return traversal


if __name__ == "__main__":
    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )

    print("Testing preorder traversal")
    print(preorder_traveral(root, ""))

    print("Testing inorder traversal")
    print(inorder_traversal(root, ""))

    print("Testing postorder traversal")
    print(postorder_traversal(root, ""))
