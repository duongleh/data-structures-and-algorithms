from linked_list import LinkedList, Node, run_test


class DoublyLinkedList(LinkedList):
    def add_at_head(self, node: Node) -> None:
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def add_at_tail(self, node: Node) -> None:
        if self.length == 0:
            return self.add_at_head(node)

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1

    def insert_before(self, node: Node, node_to_insert: Node) -> None:
        if not self.is_node_in_list(node):
            raise Exception("Invalid node")

        if node == self.head:
            return self.add_at_head(node_to_insert)

        node_to_insert.prev = node.prev
        node_to_insert.next = node
        node_to_insert.prev.next = node_to_insert
        node.prev = node_to_insert
        self.length += 1

    def insert_after(self, node: Node, node_to_insert: Node) -> None:
        if not self.is_node_in_list(node):
            raise Exception("Invalid node")

        if node == self.tail:
            return self.add_at_tail(node_to_insert)

        node_to_insert.prev = node
        node_to_insert.next = node.next
        node_to_insert.next.prev = node_to_insert
        node.next = node_to_insert
        self.length += 1

    def delete_head(self) -> None:
        if not self.head:
            return

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

        self.length -= 1

    def delete_tail(self) -> None:
        if not self.tail:
            return

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        self.length -= 1

    def delete_node(self, node: Node) -> None:
        if node == self.head:
            return self.delete_head()

        if node == self.tail:
            return self.delete_tail()

        if not self.is_node_in_list(node):
            raise Exception("Invalid node")

        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def reverse_list(self):
        current_node = self.head

        while current_node is not None:
            # Reverse the order
            current_node.next, current_node.prev = current_node.prev, current_node.next

            # Move the cursor
            current_node = current_node.prev

        self.head, self.tail = self.tail, self.head


if __name__ == "__main__":
    run_test(DoublyLinkedList)
