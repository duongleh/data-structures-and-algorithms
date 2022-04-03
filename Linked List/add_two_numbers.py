# https://leetcode.com/problems/add-two-numbers
# O(max(N, M)) T | O(max(N, M)) S

from typing import Optional

from linked_list import Node


def add_two_numbers(
    linked_list_one: Optional[Node],
    linked_list_two: Optional[Node],
) -> Optional[Node]:
    carry = 0
    root_node = current_node = Node(0)
    while linked_list_one or linked_list_two or carry:
        digit_sum = 0
        if linked_list_one:
            digit_sum += linked_list_one.val
            linked_list_one = linked_list_one.next
        if linked_list_two:
            digit_sum += linked_list_two.val
            linked_list_two = linked_list_two.next

        digit_sum += carry
        carry = digit_sum // 10
        digit_sum %= 10

        current_node.next = Node(digit_sum)
        current_node = current_node.next

    return root_node.next
