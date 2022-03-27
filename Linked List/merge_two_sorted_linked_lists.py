# https://leetcode.com/problems/merge-two-sorted-lists/
# O(M+N) TS

from typing import Optional

from linked_list import Node


def merge_two_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    head = sorted_list = Node(0)

    while list1 and list2:
        if list1.val <= list2.val:
            sorted_list.next = list1
            list1 = list1.next
        else:
            sorted_list.next = list2
            list2 = list2.next
        sorted_list = sorted_list.next

    sorted_list.next = list1 or list2

    return head.next
