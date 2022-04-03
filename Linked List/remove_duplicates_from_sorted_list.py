# https://leetcode.com/problems/remove-duplicates-from-sorted-list
# O(N) T | O(1) S

from typing import Optional

from linked_list import Node


def delete_duplicates(head: Optional[Node]) -> Optional[Node]:
    current = head
    while current is not None:
        next_distinct_node = current.next
        while next_distinct_node and current.value == next_distinct_node.value:
            next_distinct_node = next_distinct_node.next

        current.next = next_distinct_node
        current = next_distinct_node

    return head
