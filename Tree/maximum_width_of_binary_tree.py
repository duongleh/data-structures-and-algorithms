# https://leetcode.com/problems/maximum-width-of-binary-tree
# O(N) TS

from typing import Optional

from binary_tree import TreeNode


def maximum_width_of_binary_tree(root: Optional[TreeNode]) -> int:
    nodes_index = []
    queue = [(root, 0)] if root else []
    max_width = 1
    while queue:
        for _ in range(len(queue)):
            node, index = queue.pop(0)
            nodes_index.append(index)
            if node.left:
                queue.append((node.left_child, index * 2 + 1))
            if node.right:
                queue.append((node.right_child, index * 2 + 2))

        if len(nodes_index) > 1:
            max_width = max(max_width, nodes_index[-1] - nodes_index[0] + 1)
        nodes_index = []

    return max_width
