# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# O(N) T | O(1) S

from typing import Optional

from linked_list import Node


def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
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
