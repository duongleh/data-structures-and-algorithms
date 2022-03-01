# https://leetcode.com/problems/same-tree
# O(N) T - O(N) S

from typing import Optional

from Tree.binary_tree import TreeNode


class SameTree:
    def recursive_traverse(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
        if not left_node and not right_node:
            return True

        if not left_node or not right_node:
            return False

        if left_node.value != right_node.value:
            return False

        is_left_subtree_identical = self.recursive_traverse(left_node.left_child, right_node.left_child)
        is_right_subtree_identical = self.recursive_traverse(left_node.right_child, right_node.right_child)

        return is_left_subtree_identical and is_right_subtree_identical

    def iterative_traverse(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
        queue = [(left_node, right_node)]

        while queue:
            left_node, right_node = queue.pop()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if left_node.value != right_node.value:
                return False

            queue.append((left_node.left_child, right_node.left_child))
            queue.append((left_node.right_child, right_node.right_child))

        return True
