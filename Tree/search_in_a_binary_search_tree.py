# https://leetcode.com/problems/search-in-a-binary-search-tree

from typing import Optional

from binary_tree import TreeNode


# O(H) TS
def search_in_a_binary_search_tree_recursion(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None

    if root.val == target:
        return root
    elif target > root.val:
        return search_in_a_binary_search_tree_recursion(root.right, target)
    else:
        return search_in_a_binary_search_tree_recursion(root.left, target)


# O(H) T | O(1) S
def search_in_a_binary_search_tree_iteration(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None

    while root:
        if root.val == target:
            return root
        elif target > root.val:
            root = root.right
        else:
            root = root.left

    return None
