# https://www.algoexpert.io/questions/Min%20Heap%20Construction


class MinHeap:
    def __init__(self, array):
        self.heap = []
        self.build_heap(array)

    def left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def swap(self, left_index: int, right_index: int) -> None:
        self.heap[left_index], self.heap[right_index] = self.heap[right_index], self.heap[left_index]

    # O(N) TS
    def build_heap(self, array: list[int]) -> None:
        """Building a Min Heap from an input array of integers."""
        self.heap = array.copy()
        last_parent_index = self.parent_index(len(self.heap) - 1)
        for node_index in range(last_parent_index, -1, -1):
            self.sift_down(node_index)

    # O(logN) T | O(1) S
    def sift_down(self, node_index: int) -> int:
        """Sifting integers down the heap."""
        left_child_index = self.left_child_index(node_index)
        right_child_index = self.right_child_index(node_index)
        min_index = node_index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[node_index]:
            min_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index

        if min_index == node_index:
            return node_index

        self.swap(node_index, min_index)
        return self.sift_down(min_index)

    # O(logN) T | O(1) S
    def sift_up(self, node_index: int) -> int:
        """Sifting integers up the heap."""
        parent_index = self.parent_index(node_index)

        if self.heap[parent_index] < self.heap[node_index]:
            return node_index

        self.swap(node_index, parent_index)
        return self.sift_up(parent_index)

    # O (1) TS
    def peek(self) -> int:
        """Peeking at the heap's minimum / root value."""
        return self.heap[0] if self.heap else None

    # O(logN) T | O(1) S
    def remove(self) -> int:
        """Removing the heap's minimum / root value."""
        self.swap(0, -1)
        removed_value = self.heap.pop()
        self.sift_down(0)
        return removed_value

    # O(logN) T | O(1) S
    def insert(self, value: int) -> int:
        """Inserting integers in the heap."""
        self.heap.append(value)
        return self.sift_up(len(self.heap) - 1)
