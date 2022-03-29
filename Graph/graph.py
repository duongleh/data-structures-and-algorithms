import json
from typing import Optional, Union


class AdjacencyListGraph:
    def __init__(self, is_directed: bool = False, is_weighted: bool = False) -> None:
        self.graph: dict[int, list[Union[int, list]]] = {}
        self.is_directed = is_directed
        self.is_weighted = is_weighted

    def __str__(self) -> str:
        return json.dumps(self.graph)

    def add_vertex(self, vertex: int) -> None:
        """Insert a new Vertex."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex_1: int, vertex_2: int, weight: int = 0) -> None:
        """Insert and return a new Edge from vertex_1 to vertex_2 with auxiliary element weight."""
        for vertex in [vertex_1, vertex_2]:
            self.add_vertex(vertex)

        if self.is_edge_existed(vertex_1, vertex_2):
            return

        self.graph[vertex_1].append([vertex_2, weight] if self.is_weighted else vertex_2)
        if not self.is_directed:
            self.graph[vertex_2].append([vertex_1, weight] if self.is_weighted else vertex_1)

    def is_edge_existed(self, vertex_1: int, vertex_2: int) -> bool:
        """Return the boolean value representing the connection between 2 vertices"""
        for adjacent_vertex in self.get_adjacent_vertices(vertex_1):
            if (adjacent_vertex[0] if self.is_weighted else adjacent_vertex) == vertex_2:
                return True
        return False

    def get_edge_weight(self, vertex_1: int, vertex_2: int) -> Optional[int]:
        """Return the weight of the edge from vertex_1 to vertex_2, or None if not adjacent."""
        if not self.is_weighted:
            return None

        for adjacent_vertex, weight in self.get_adjacent_vertices(vertex_1):
            if adjacent_vertex == vertex_2:
                return weight

        return None

    def set_edge_weight(self, vertex_1: int, vertex_2: int, weight: int = 0) -> None:
        """Set the weight of the edge from vertex_1 to vertex_2 if adjacent."""
        if not self.is_weighted:
            return

        if not self.is_edge_existed(vertex_1, vertex_2):
            return

        for start_vertex, end_vertex in (
            [(vertex_1, vertex_2)] if self.is_directed else [(vertex_1, vertex_2), (vertex_2, vertex_1)]
        ):
            for adjacent_vertex in self.get_adjacent_vertices(start_vertex):
                if adjacent_vertex[0] == end_vertex:
                    adjacent_vertex[1] = weight

    def vertex_count(self) -> int:
        """Return the number of vertices in the graph."""
        return len(self.graph.keys())

    def edge_count(self) -> int:
        """Return the number of edges in the graph."""
        total_edges = sum(len(adjacent_vertices) for adjacent_vertices in self.graph.values())
        return total_edges if self.is_directed else total_edges // 2

    def vertices(self) -> list[int]:
        """Return a list of all vertices of the graph."""
        return list(self.graph.keys())

    def edges(self) -> list[tuple]:
        """Return a list of all edges of the graph."""
        edges = []
        for vertex, adjacent_vertices in self.graph.items():
            for adjacent_vertex in adjacent_vertices:
                edges.append((vertex, *adjacent_vertex) if self.is_weighted else (vertex, adjacent_vertex))
        return edges

    def get_adjacent_vertices(self, vertex: int) -> list[Union[int, list]]:
        """Return a list of all vertices connecting with the vertex."""
        return self.graph.get(vertex, [])

    def in_degree(self, vertex: int) -> Optional[int]:
        """Return number of incoming edges incident to the vertex in the graph."""
        if not self.is_directed:
            return None

        in_degree_total = 0
        for vertex_value, adjacent_vertices in self.graph.items():
            if vertex_value == vertex:
                continue

            for adjacent_vertex in adjacent_vertices:
                if (adjacent_vertex[0] if self.is_weighted else adjacent_vertex) == vertex:
                    in_degree_total += 1

        return in_degree_total

    def out_degree(self, vertex: int) -> Optional[int]:
        """Return number of outgoing edges incident to the vertex in the graph."""
        if not self.is_directed:
            return None

        return len(self.get_adjacent_vertices(vertex))

    def degree(self, vertex: int) -> int:
        """Return number of incident edges to the vertex in the graph."""
        if self.is_directed:
            return self.in_degree(vertex) + self.out_degree(vertex)

        return len(self.get_adjacent_vertices(vertex))


if __name__ == "__main__":
    for is_directed, is_weighted in [(False, False), (True, False), (False, True), (True, True)]:
        graph = AdjacencyListGraph(is_weighted=is_weighted, is_directed=is_directed)
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 2)
        graph.add_edge(4, 3, 3)
        graph.add_edge(4, 5, 4)

        assert graph.is_edge_existed(0, 1) is False
        assert graph.is_edge_existed(1, 2) is True
        assert graph.is_edge_existed(2, 1) is False if is_directed else True

        assert graph.get_edge_weight(0, 1) is None
        assert graph.get_edge_weight(1, 2) == (1 if is_weighted else None)
        assert graph.get_edge_weight(2, 1) == (1 if is_weighted and not is_directed else None)

        graph.set_edge_weight(1, 2, 5)
        assert graph.get_edge_weight(1, 2) == (5 if is_weighted else None)
        assert graph.get_edge_weight(2, 1) == (5 if is_weighted and not is_directed else None)

        assert graph.vertex_count() == 6
        assert graph.edge_count() == 4
        assert graph.vertices() == [0, 1, 2, 3, 4, 5]

        assert graph.in_degree(2) == (1 if is_directed else None)
        assert graph.out_degree(2) == (1 if is_directed else None)
        assert graph.degree(2) == 2

        if not is_directed and not is_weighted:
            assert graph.edges() == [
                (1, 2),
                (2, 1),
                (2, 3),
                (3, 2),
                (3, 4),
                (4, 3),
                (4, 5),
                (5, 4),
            ]
            assert graph.get_adjacent_vertices(2) == [1, 3]
        elif is_directed and not is_weighted:
            assert graph.edges() == [
                (1, 2),
                (2, 3),
                (4, 3),
                (4, 5),
            ]
            assert graph.get_adjacent_vertices(2) == [3]
        elif not is_directed and is_weighted:
            assert graph.edges() == [
                (1, 2, 5),
                (2, 1, 5),
                (2, 3, 2),
                (3, 2, 2),
                (3, 4, 3),
                (4, 3, 3),
                (4, 5, 4),
                (5, 4, 4),
            ]
            assert graph.get_adjacent_vertices(2) == [[1, 5], [3, 2]]
        elif is_directed and is_weighted:
            assert graph.edges() == [
                (1, 2, 5),
                (2, 3, 2),
                (4, 3, 3),
                (4, 5, 4),
            ]
            assert graph.get_adjacent_vertices(2) == [[3, 2]]
