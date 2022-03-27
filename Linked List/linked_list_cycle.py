# https://leetcode.com/problems/linked-list-cycle/
# O(N) TS

from typing import Optional

from linked_list import Node


def has_cycle(current: Optional[Node]) -> bool:
    node_frequencies = {}
    while current is not None:
        if current not in node_frequencies:
            node_frequencies[current] = 1
        else:
            return True
        current = current.next
    return False
