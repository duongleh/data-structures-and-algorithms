from typing import Optional

from binary_tree import TreeNode


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# O(N) TS
def construct_from_preorder_and_inorder(
    preorder: list[int],
    inorder: list[int],
) -> Optional[TreeNode]:
    if not inorder:
        return None

    root_node = TreeNode(preorder.pop(0))

    root_index = inorder.index(root_node.value)

    root_node.left = construct_from_preorder_and_inorder(preorder, inorder[0:root_index])
    root_node.right = construct_from_preorder_and_inorder(preorder, inorder[root_index + 1 :])

    return root_node


# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
# O(N) TS
def construct_from_inorder_and_postorder(
    inorder: list[int],
    postorder: list[int],
) -> Optional[TreeNode]:
    if not inorder:
        return None

    root_node = TreeNode(postorder.pop())

    root_index = inorder.index(root_node.value)

    root_node.right = construct_from_inorder_and_postorder(inorder[root_index + 1 :], postorder)
    root_node.left = construct_from_inorder_and_postorder(inorder[0:root_index], postorder)

    return root_node
