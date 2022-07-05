from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int = 0
    left_child: TreeNode = None
    right_child: TreeNode = None

    def is_leaf(self) -> bool:
        return self.left_child is None and self.right_child is None
