# https://leetcode.com/problems/maximum-depth-of-binary-tree
# O(N) TS

from typing import Optional

from binary_tree import TreeNode


class MaximumDepthBinaryTree:
    def recursive_traverse(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return depth

        depth += 1

        if root.left_child is root.right_child is None:
            return depth

        left_depth = self.recursive_traverse(root.left_child, depth)
        right_depth = self.recursive_traverse(root.right_child, depth)
        return max(left_depth, right_depth)

    def iterative_traverse(self, root: Optional[TreeNode]) -> int:
        queue = [root] if root else None
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left_child:
                    queue.append(node.left_child)
                if node.right_child:
                    queue.append(node.right_child)

        return depth
