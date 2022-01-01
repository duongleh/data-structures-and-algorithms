# https://leetcode.com/problems/linked-list-cycle/
# O(N) TS

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, current: Optional[ListNode]) -> bool:
        node_frequencies = {}
        while current is not None:
            if current not in node_frequencies:
                node_frequencies[current] = 1
            else:
                return True
            current = current.next
        return False
