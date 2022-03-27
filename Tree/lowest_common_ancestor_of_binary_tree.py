# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# O(N) T | O(N) S

from binary_tree import TreeNode


def lowest_common_ancestor_of_binary_tree(
    self,
    root: TreeNode,
    p: TreeNode,
    q: TreeNode,
) -> TreeNode:
    if not root:
        return None

    if root in [p, q]:
        return root

    left_common_ancestor = self.lowestCommonAncestor(root.left_child, p, q)
    right_common_ancestor = self.lowestCommonAncestor(root.right_child, p, q)

    if left_common_ancestor and right_common_ancestor:
        return root

    return left_common_ancestor or right_common_ancestor
