# https://leetcode.com/problems/insert-into-a-binary-search-tree
# O(H) T | O(1) S

from typing import Optional

from binary_tree import TreeNode


def insert_into_a_binary_search_tree(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(target)

    if target > root.value:
        root.right_child = insert_into_a_binary_search_tree(root.right_child, target)
    else:
        root.left_child = insert_into_a_binary_search_tree(root.left_child, target)

    return root
