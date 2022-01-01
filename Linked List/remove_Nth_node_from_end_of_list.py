# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# O(N) T - O(1) S

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        future = current = head
        for _ in range(n):
            future = future.next

        if not future:
            return head.next

        while future.next is not None:
            current = current.next
            future = future.next

        current.next = current.next.next
        return head
