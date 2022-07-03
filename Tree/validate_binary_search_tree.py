# https://leetcode.com/problems/validate-binary-search-tree
# O(N) TS

from math import inf
from binary_tree import TreeNode


def validate_binary_search_tree_inorder_traversal(root: TreeNode) -> bool:
    previous_node = -inf

    def traverse_inorder(root: TreeNode):
        if root.left and traverse_inorder(root.left) is False:
            return False

        nonlocal previous_node
        if root.val <= previous_node:
            return False
        previous_node = root.val

        if root.right and traverse_inorder(root.right) is False:
            return False

        return True

    return traverse_inorder(root)


def validate_binary_search_tree_valid_range(
    root: TreeNode,
    low: int = -inf,
    high: int = inf,
) -> bool:
    if not root:
        return True

    if root.val <= low or root.val >= high:
        return False

    return (
        validate_binary_search_tree_valid_range(root.left, low, root.val)
        and validate_binary_search_tree_valid_range(root.right, root.val, high),
    )
