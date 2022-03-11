from typing import Optional

from Tree.binary_tree import TreeNode


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# O(N) T - O(N) S
def construct_from_preorder_and_inorder(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not inorder:
        return None

    root_node = TreeNode(preorder.pop(0))

    root_index = inorder.index(root_node.value)

    root_node.left = construct_from_preorder_and_inorder(preorder, inorder[0:root_index])
    root_node.right = construct_from_preorder_and_inorder(preorder, inorder[root_index + 1 :])

    return root_node
