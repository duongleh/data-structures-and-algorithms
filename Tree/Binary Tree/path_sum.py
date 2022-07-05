# https://leetcode.com/problems/path-sum
# O(N) TS


from typing import Optional

from binary_tree import TreeNode


def path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    target_sum -= root.value

    if not root.left_child and not root.right_child:
        return target_sum == 0

    return path_sum(root.left_child, target_sum) or path_sum(root.right_child, target_sum)
