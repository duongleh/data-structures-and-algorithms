# https://www.lintcode.com/problem/inorder-successor-in-bst
# O(H) T | O(1) S


from typing import Optional

from binary_tree import TreeNode


def inorder_successor_in_bst(root: Optional[TreeNode], target: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return None

    successor = None
    while root is not None:
        if root.value > target.value:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor
