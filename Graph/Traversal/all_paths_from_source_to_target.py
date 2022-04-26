# https://leetcode.com/problems/all-paths-from-source-to-target
# O(2^V*V) T | O(V+E) S

from Graph.graph import AdjacencyListGraph


def all_paths_from_source_to_target(graph: AdjacencyListGraph) -> list[list[int]]:
    def dfs(
        graph: AdjacencyListGraph,
        source: int,
        target: int,
        path: list[int],
        paths: list[list[int]],
    ):
        path.append(source)

        if source == target:
            paths.append(path)
            return

        for adjacent_vertex in graph.get_adjacent_vertices(source):
            dfs(graph, adjacent_vertex, target, [*path], paths)

        return paths

    return dfs(graph, 0, graph.vertex_count() - 1, [], [])
