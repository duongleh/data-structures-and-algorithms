# https://leetcode.com/problems/course-schedule-ii
# O(V+E) TS

from graph import AdjacencyListGraph


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = AdjacencyListGraph(is_directed=True)
    indegree = [0] * num_courses

    for end_course, start_course in prerequisites:
        graph.add_edge(start_course, end_course)
        indegree[end_course] += 1

    topological_order = []
    find_path(graph, indegree, topological_order, [])
    return topological_order if len(topological_order) == num_courses else []


def find_path(
    graph: AdjacencyListGraph,
    indegree: list[int],
    topological_order: list[int],
    queue: list[int],
):
    for vertex, degree in enumerate(indegree):
        if degree == 0:
            queue.append(vertex)

    while queue:
        vertex = queue.pop(0)
        topological_order.append(vertex)

        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            indegree[adjacent_vertex] -= 1
            if indegree[adjacent_vertex] == 0:
                queue.append(adjacent_vertex)
