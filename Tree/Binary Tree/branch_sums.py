# https://www.algoexpert.io/questions/Branch%20Sums
# O(N) TS


from typing import Optional

from binary_tree import TreeNode


def branch_sums(
    root: Optional[TreeNode],
    running_sum: int = 0,
    sums: list[int] = None,
) -> list[int]:
    if sums is None:
        sums = []

    if not root:
        return sums

    running_sum += root.value

    if root.left_child:
        branch_sums(root.left_child, running_sum, sums)

    if root.right_child:
        branch_sums(root.right_child, running_sum, sums)

    if not root.left_child and not root.right_child:
        sums.append(running_sum)

    return sums
