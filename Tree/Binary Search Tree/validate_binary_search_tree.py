# https://leetcode.com/problems/validate-binary-search-tree
# O(N) TS

from math import inf
from binary_tree import TreeNode


def validate_binary_search_tree_inorder_traversal(root: TreeNode) -> bool:
    previous_node = -inf

    def traverse_inorder(root: TreeNode):
        if root.left_child and traverse_inorder(root.left_child) is False:
            return False

        nonlocal previous_node
        if root.value <= previous_node:
            return False
        previous_node = root.value

        if root.right_child and traverse_inorder(root.right_child) is False:
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

    if root.value <= low or root.value >= high:
        return False

    return (
        validate_binary_search_tree_valid_range(root.left_child, low, root.value)
        and validate_binary_search_tree_valid_range(root.right_child, root.value, high),
    )
