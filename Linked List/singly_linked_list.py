from typing import Optional

from linked_list import LinkedList, Node, run_test


class SinglyLinkedList(LinkedList):
    @property
    def tail(self) -> Node:
        if not self.head:
            return None

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        return current_node

    @tail.setter
    def tail(self, value) -> Node:
        pass

    def _get_the_previous_node_of(self, node: Node) -> Optional[Node]:
        if not self.head:
            return None

        current_node = self.head
        while current_node.next is not None:
            if current_node.next == node:
                return current_node
            current_node = current_node.next

        return None

    def add_at_head(self, node: Node) -> None:
        node.next = self.head
        self.head = node
        self.length += 1

    def add_at_tail(self, node: Node) -> None:
        if not self.head:
            return self.add_at_head(node)

        self.tail.next = node
        self.length += 1

    def insert_before(self, node: Node, node_to_insert: Node) -> None:
        if node == self.head:
            return self.add_at_head(node_to_insert)

        if not self.is_node_in_list(node):
            raise Exception('Invalid node')

        previous_node = self._get_the_previous_node_of(node)

        node_to_insert.next = previous_node.next
        previous_node.next = node_to_insert
        self.length += 1

    def insert_after(self, node: Node, node_to_insert: Node) -> None:
        if not self.is_node_in_list(node):
            raise Exception('Invalid node')

        node_to_insert.next = node.next
        node.next = node_to_insert
        self.length += 1

    def delete_head(self) -> None:
        if not self.head:
            return None

        self.head = self.head.next
        self.length -= 1

    def delete_tail(self) -> None:
        if not self.head.next:
            return self.delete_head()

        second_to_last_node = self._get_the_previous_node_of(self.tail)
        second_to_last_node.next = None
        self.length -= 1

    def delete_node(self, node: Node) -> None:
        if node == self.head:
            return self.delete_head()

        if not self.is_node_in_list(node):
            raise Exception('Invalid node')

        previous_node = self._get_the_previous_node_of(node)
        previous_node.next = node.next
        self.length -= 1

    def reverse_list(self):
        prev_node = None
        current_node = self.head
        next_node = current_node.next

        while current_node is not None:
            # Reverse the order
            current_node.next = prev_node

            # Move the cursor
            prev_node = current_node
            current_node = next_node

            if current_node is None:
                self.head = prev_node
            else:
                next_node = next_node.next


if __name__ == '__main__':
    run_test(SinglyLinkedList)
