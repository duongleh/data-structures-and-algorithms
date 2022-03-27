# https://leetcode.com/problems/path-sum
# O(N) T | O(N) S


from typing import Optional

from binary_tree import TreeNode


def path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    target_sum -= root.val

    if not root.left and not root.right:
        return target_sum == 0

    return path_sum(root.left, target_sum) or path_sum(root.right, target_sum)
