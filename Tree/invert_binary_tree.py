# https://leetcode.com/problems/invert-binary-tree
# O(N) T - O(N) S

from typing import Optional

from Tree.binary_tree import TreeNode


class InvertBinaryTree:
    def recursive_traverse(self, root: Optional[TreeNode]) -> TreeNode:
        if root:
            root.left_child, root.right_child = root.right_child, root.left_child
            self.invertTree(root.left_child)
            self.invertTree(root.right_child)

        return root

    def iterative_traverse(self, root: Optional[TreeNode]) -> TreeNode:
        queue = [root] if root else []
        while queue:
            node = queue.pop()
            node.left_child, node.right_child = node.right_child, node.left_child

            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)

        return root
