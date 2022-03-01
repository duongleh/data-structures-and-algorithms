# https://leetcode.com/problems/binary-tree-level-order-traversal
# O(N) T - O(H) S (H is the height of the Binary Tree)

from typing import Optional

from Tree.binary_tree import TreeNode


class DepthFirstTraversal:
    def recursive_traverse(
        self,
        root: Optional[TreeNode] = None,
        queue: list[TreeNode] = None,
        traversed_list: list[list[int]] = None,
    ) -> list[list[int]]:
        if queue is None:
            queue = [root] if root else []

        if traversed_list is None:
            traversed_list = []

        if not queue:
            return traversed_list

        traversed_list.append([])

        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)

            traversed_list[-1].append(node.value)

        self.recursive_traverse(queue=queue, traversed_list=traversed_list)

        return traversed_list

    def iterative_traverse(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = [root] if root else []
        traversed_list = []

        while queue:
            nodes_by_depth = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left_child:
                    queue.append(node.left_child)
                if node.right_child:
                    queue.append(node.right_child)

                nodes_by_depth.append(node.value)

            traversed_list.append(nodes_by_depth)

        return traversed_list
