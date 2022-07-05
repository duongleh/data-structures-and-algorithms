# https://leetcode.com/problems/delete-node-in-a-bst
# O(H) TS

from typing import Optional

from binary_tree import TreeNode


def delete_node_in_a_bst(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None

    if target > root.val:
        root.right = delete_node_in_a_bst(root.right, target)
    elif target < root.val:
        root.left = delete_node_in_a_bst(root.left, target)
    else:
        # The target node has no child, we can simply remove the node
        if not root.left and not root.right:
            return None

        # The target node has one child, we can use its child to replace itself.
        if not root.left or not root.right:
            return root.left or root.right

        # The target node has two children, replace the node with its in-order successor node and delete that node
        # Find the node with min value in the right subtree, aka the in-order successor node
        successor_node = root.right
        while successor_node.left:
            successor_node = successor_node.left

        root.val = successor_node.val
        root.right = delete_node_in_a_bst(root.right, successor_node.val)

    return root
