# https://leetcode.com/problems/delete-node-in-a-bst
# O(H) TS

from typing import Optional

from binary_tree import TreeNode


def delete_node_in_a_bst(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None

    if target > root.value:
        root.right_child = delete_node_in_a_bst(root.right_child, target)
    elif target < root.value:
        root.left_child = delete_node_in_a_bst(root.left_child, target)
    else:
        # The target node has no child, we can simply remove the node
        if not root.left_child and not root.right_child:
            return None

        # The target node has one child, we can use its child to replace itself.
        if not root.left_child or not root.right_child:
            return root.left_child or root.right_child

        # The target node has two children, replace the node with its in-order successor node and delete that node
        # Find the node with min value in the right subtree, aka the in-order successor node
        successor_node = root.right_child
        while successor_node.left_child:
            successor_node = successor_node.left_child

        root.value = successor_node.value
        root.right_child = delete_node_in_a_bst(root.right_child, successor_node.value)

    return root
