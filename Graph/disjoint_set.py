from abc import abstractmethod
from typing import Optional


class DisjointSet:
    def __init__(self, size: int):
        self.roots = list(range(size))

    @abstractmethod
    def find(self, vertex: int) -> int:
        pass

    @abstractmethod
    def union(self, vertex_1: int, vertex_2: int) -> Optional[int]:
        pass

    def is_connected(self, vertex_1: int, vertex_2: int) -> bool:
        return self.find(vertex_1) == self.find(vertex_2)


class QuickFind(DisjointSet):
    """
    find: O(1) T
    union: O(N) T
    is_connected: O(1) T
    Space: O(N) S
    """

    def find(self, vertex: int) -> int:
        return self.roots[vertex]

    def union(self, vertex_1: int, vertex_2: int) -> Optional[int]:
        root_vertex_1 = self.find(vertex_1)
        root_vertex_2 = self.find(vertex_2)
        if root_vertex_1 == root_vertex_2:
            return None

        for index, root_vertex in enumerate(self.roots):
            if root_vertex == root_vertex_2:
                self.roots[index] = root_vertex_1

        return root_vertex_1


class QuickUnion(DisjointSet):
    """
    find: O(N) T
    union: O(N) T
    is_connected: O(N) T
    Space: O(N) S

    The union and connected operations both depend on the find operation.
    In the worst case scenario, the tree's height is equal to the number of vertices,
    which is the number of operations to find the root of the input vertex.
    """

    def find(self, vertex: int) -> int:
        while vertex != self.roots[vertex]:
            vertex = self.roots[vertex]
        return vertex

    def union(self, vertex_1: int, vertex_2: int) -> Optional[int]:
        root_vertex_1 = self.find(vertex_1)
        root_vertex_2 = self.find(vertex_2)
        if root_vertex_1 == root_vertex_2:
            return None

        self.roots[root_vertex_2] = root_vertex_1
        return root_vertex_1


class UnionByRank(QuickUnion):
    """
    find: O(log(N)) T
    union: O(log(N)) T
    is_connected: O(log(N)) T
    Space: O(N) S

    The height of the tree only increases when 2 same size sets are unioned.
    In the worst case scenario, we repeatedly union components of equal rank (doubling the input each joining time),
    the height will only increase by one, producing the logarithmic running time.
    """

    def __init__(self, size: int):
        super().__init__(size)
        self.ranks = [1] * size

    def union(self, vertex_1: int, vertex_2: int) -> Optional[int]:
        root_vertex_1 = self.find(vertex_1)
        root_vertex_2 = self.find(vertex_2)
        if root_vertex_1 == root_vertex_2:
            return None

        if self.ranks[root_vertex_1] < self.ranks[root_vertex_2]:
            self.roots[root_vertex_1] = root_vertex_2
            return root_vertex_2

        if self.ranks[root_vertex_1] == self.ranks[root_vertex_2]:
            self.ranks[root_vertex_1] += 1

        self.roots[root_vertex_2] = root_vertex_1
        return root_vertex_1


class OptimizedPathCompression(QuickUnion):
    """
    find: O(N) T
    union: O(N) T
    is_connected: O(N) T
    Space: O(N) S

    In the worst case scenario, it would be O(N) time when the tree is skewed.
    However, on average, the time complexity will be O(log(N)).
    """

    def find(self, vertex: int) -> int:
        if vertex == self.roots[vertex]:
            return vertex
        self.roots[vertex] = self.find(self.roots[vertex])
        return self.roots[vertex]


class UnionFind(UnionByRank, OptimizedPathCompression):
    """
    find: O(α(N)) T
    union: O(α(N)) T
    is_connected: O(α(N)) T
    Space: O(N) S

    All operation will take O(α(N)) time on average. α refers to the Inverse Ackermann function.
    In practice, we assume it's a constant. In other words, O(α(N)) is regarded as O(1) on average.
    """
