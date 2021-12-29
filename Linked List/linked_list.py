import sys
import unittest
from abc import ABC, abstractmethod
from typing import Optional


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        next_value = self.next.value if self.next else None
        prev_value = self.prev.value if self.prev else None
        return f'Current value {self.value}, next {next_value}, prev {prev_value}'


class LinkedList(ABC):
    def __init__(self):
        """
        Initialize linked list data structure
        """
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        current_node = self.head
        linked_list = []
        while current_node is not None:
            linked_list.append(str(current_node.value))
            current_node = current_node.next
        return ', '.join(linked_list)

    @abstractmethod
    def add_at_head(self, node: Node) -> None:
        """
        Add a node before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        pass

    @abstractmethod
    def add_at_tail(self, node: Node) -> None:
        """
        Append a node to the last element of the linked list.
        """
        pass

    @abstractmethod
    def insert_before(self, node: Node, node_to_insert: Node) -> None:
        pass

    @abstractmethod
    def insert_after(self, node: Node, node_to_insert: Node) -> None:
        pass

    def insert_at_index(self, index: int, node: Node) -> None:
        """
        Add a node before the index-th node in the linked list.
        If index equals the length of the new linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:
            raise Exception('Invalid index')

        if index == 0:
            return self.add_at_head(node)

        current_node = self.head
        for _ in range(index-1):
            current_node = current_node.next

        self.insert_after(current_node, node)

    @abstractmethod
    def delete_head(self) -> None:
        pass

    @abstractmethod
    def delete_tail(self) -> None:
        pass

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            raise Exception('Invalid index')

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        self.delete_node(current_node)

    @abstractmethod
    def delete_node(self, node: Node) -> None:
        pass

    def delete_node_with_value(self, value: int) -> None:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return self.delete_node(current_node)
            current_node = current_node.next
        raise Exception('Invalid value')

    def get_at_index(self, index: int) -> Optional[Node]:
        """
        Get the node of the index-th node in the linked list. If the index is invalid, return None.
        """
        if index < 0 or index >= self.length:
            return None

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def is_value_in_list(self, value: int) -> bool:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def is_node_in_list(self, node: Node) -> bool:
        current_node = self.head
        while current_node is not None:
            if current_node == node:
                return True
            current_node = current_node.next
        return False

    @abstractmethod
    def reverse_list(self) -> None:
        pass


def run_test(linked_list_class):
    test_loader = unittest.TestLoader()
    test_case_names = test_loader.getTestCaseNames(TestLinkedList)
    suite = unittest.TestSuite()
    for test_case_name in test_case_names:
        suite.addTest(TestLinkedList(test_case_name, linked_list_class))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


class TestLinkedList(unittest.TestCase):
    def __init__(self, test_case_name, linked_list_class):
        super(TestLinkedList, self).__init__(test_case_name)
        self.linked_list_class = linked_list_class

    def setUp(self):
        self.node_0 = Node(0)
        self.node_1 = Node(1)
        self.node_2 = Node(2)

    def test_is_element_in_list(self):
        linked_list: LinkedList = self.linked_list_class()
        linked_list.add_at_tail(self.node_0)
        linked_list.add_at_tail(self.node_1)
        linked_list.add_at_tail(self.node_2)

        self.assertTrue(linked_list.is_value_in_list(0))
        self.assertTrue(linked_list.is_value_in_list(1))
        self.assertTrue(linked_list.is_value_in_list(2))
        self.assertFalse(linked_list.is_value_in_list(3))

        self.assertTrue(linked_list.is_node_in_list(self.node_0))
        self.assertTrue(linked_list.is_node_in_list(self.node_1))
        self.assertTrue(linked_list.is_node_in_list(self.node_2))
        self.assertFalse(linked_list.is_node_in_list(Node(3)))

    def test_get_node_at_specific_index(self):
        linked_list: LinkedList = self.linked_list_class()
        linked_list.add_at_tail(self.node_0)
        linked_list.add_at_tail(self.node_1)
        linked_list.add_at_tail(self.node_2)

        self.assertEqual(linked_list.get_at_index(0).value, 0)
        self.assertEqual(linked_list.get_at_index(1).value, 1)
        self.assertEqual(linked_list.get_at_index(2).value, 2)
        self.assertEqual(linked_list.get_at_index(3), None)

    def test_insert_node(self):
        #  Add at head and tail
        self.linked_list: LinkedList = self.linked_list_class()
        self.assertEqual(str(self.linked_list), '')
        self.assertEqual(self.linked_list.length, 0)

        self.linked_list.add_at_head(self.node_1)
        self.linked_list.add_at_head(self.node_0)
        self.linked_list.add_at_tail(self.node_2)

        self.assertEqual(str(self.linked_list), '0, 1, 2')
        self.assertEqual(self.linked_list.length, 3)

        # Insert before a given node
        self.node_3 = Node(3)
        self.linked_list.insert_before(self.node_0, self.node_3)
        self.linked_list.insert_before(self.node_1, Node(4))
        self.linked_list.insert_before(self.node_2, Node(5))
        with self.assertRaises(Exception) as e:
            self.linked_list.insert_before(Node(0), Node(0))
        self.assertEqual((str(e.exception)), 'Invalid node')
        self.assertEqual(str(self.linked_list), '3, 0, 4, 1, 5, 2')
        self.assertEqual(self.linked_list.length, 6)

        # Insert after a given node
        self.node_6 = Node(6)
        self.linked_list.insert_after(self.node_3, self.node_6)
        self.linked_list.insert_after(self.node_1, Node(7))
        self.linked_list.insert_after(self.node_2, Node(8))
        with self.assertRaises(Exception) as e:
            self.linked_list.insert_after(Node(0), Node(0))

        self.assertEqual((str(e.exception)), 'Invalid node')
        self.assertEqual(
            str(self.linked_list), '3, 6, 0, 4, 1, 7, 5, 2, 8'
        )
        self.assertEqual(self.linked_list.length, 9)

        # Insert node at given index
        self.linked_list.insert_at_index(0, Node(9))
        self.linked_list.insert_at_index(5, Node(10))
        self.linked_list.insert_at_index(11, Node(11))
        with self.assertRaises(Exception) as e:
            self.linked_list.insert_at_index(13, Node(0))

        self.assertEqual((str(e.exception)), 'Invalid index')
        self.assertEqual(
            str(self.linked_list), '9, 3, 6, 0, 4, 10, 1, 7, 5, 2, 8, 11'
        )
        self.assertEqual(self.linked_list.length, 12)

    def test_delete_node(self):
        # Fill the linked list with nodes
        self.test_insert_node()
        self.assertEqual(
            str(self.linked_list), '9, 3, 6, 0, 4, 10, 1, 7, 5, 2, 8, 11'
        )

        #  Delete head and tail of one-node linked list
        empty_linked_list: LinkedList = self.linked_list_class()
        self.assertEqual(str(empty_linked_list), '')
        self.assertEqual(empty_linked_list.length, 0)

        empty_linked_list.add_at_head(Node(0))
        empty_linked_list.delete_head()

        assert str(empty_linked_list) == ''
        assert empty_linked_list.length == 0

        empty_linked_list.add_at_head(Node(0))
        empty_linked_list.delete_tail()

        assert str(empty_linked_list) == ''
        assert empty_linked_list.length == 0

        # Delete head and tail
        self.linked_list.delete_head()
        self.linked_list.delete_tail()
        self.assertEqual(
            str(self.linked_list), '3, 6, 0, 4, 10, 1, 7, 5, 2, 8'
        )
        self.assertEqual(self.linked_list.length, 10)

        # Delete at a given index
        self.linked_list.delete_at_index(0)
        self.linked_list.delete_at_index(5)
        self.linked_list.delete_at_index(7)
        with self.assertRaises(Exception) as e:
            self.linked_list.delete_at_index(7)

        self.assertEqual((str(e.exception)), 'Invalid index')
        self.assertEqual(
            str(self.linked_list), '6, 0, 4, 10, 1, 5, 2'
        )
        self.assertEqual(self.linked_list.length, 7)

        # Delete a give node
        self.linked_list.delete_node(self.node_6)
        self.linked_list.delete_node(self.node_1)
        self.linked_list.delete_node(self.node_2)
        with self.assertRaises(Exception) as e:
            self.linked_list.delete_node(Node(0))

        self.assertEqual((str(e.exception)), 'Invalid node')
        self.assertEqual(str(self.linked_list), '0, 4, 10, 5')
        self.assertEqual(self.linked_list.length, 4)

        # Delete node with a given value
        self.linked_list.delete_node_with_value(0)
        self.linked_list.delete_node_with_value(10)
        self.linked_list.delete_node_with_value(5)
        with self.assertRaises(Exception) as e:
            self.linked_list.delete_node_with_value(0)

        self.assertEqual((str(e.exception)), 'Invalid value')
        self.assertEqual(str(self.linked_list), '4')
        self.assertEqual(self.linked_list.length, 1)

        with self.assertRaises(Exception) as e:
            self.linked_list_class().delete_node_with_value(0)
        self.assertEqual((str(e.exception)), 'Invalid value')

    def test_reverse_linked_list(self):
        # Fill the linked list with nodes
        self.test_insert_node()
        self.assertEqual(
            str(self.linked_list), '9, 3, 6, 0, 4, 10, 1, 7, 5, 2, 8, 11'
        )

        # Reverse list
        self.linked_list.reverse_list()
        self.assertEqual(
            str(self.linked_list), '11, 8, 2, 5, 7, 1, 10, 4, 0, 6, 3, 9'
        )
