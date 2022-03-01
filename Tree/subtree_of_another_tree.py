# https://leetcode.com/problems/subtree-of-another-tree
# O(N) T - O(N) S


from typing import Optional

from Tree.binary_tree import TreeNode


def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    return self.hash(sub_root) in self.hash(root)


def hash(self, node: Optional[TreeNode]):
    if not node:
        return "#"

    left_node_hashed_value = self.hash(node.left_child)
    right_node_hashed_value = self.hash(node.right_child)

    return f"^{left_node_hashed_value}{node.value}{right_node_hashed_value}$"
