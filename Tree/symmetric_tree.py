# https://leetcode.com/problems/symmetric-tree
# O(N) T | O(N) S

from typing import Optional

from binary_tree import TreeNode


class SymmetricTree:
    def recursive_traverse(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.recursive_traverse_helper(root.left_child, root.right_child)

    def recursive_traverse_helper(
        self,
        left_node: Optional[TreeNode],
        right_node: Optional[TreeNode],
    ) -> bool:
        if not left_node and not right_node:
            return True

        if not left_node or not right_node:
            return False

        if left_node.value != right_node.value:
            return False

        is_left_subtree_symmetrical = self.recursive_traverse_helper(
            left_node.left_child,
            right_node.right_child,
        )
        is_right_subtree_symmetrical = self.recursive_traverse_helper(
            left_node.right_child,
            right_node.left_child,
        )

        return is_left_subtree_symmetrical and is_right_subtree_symmetrical

    def iterative_traverse(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [(root.left_child, root.right_child)]

        while queue:
            left_node, right_node = queue.pop()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if left_node.value != right_node.value:
                return False

            queue.append((left_node.left_child, right_node.right_child))
            queue.append((left_node.right_child, right_node.left_child))

        return True
