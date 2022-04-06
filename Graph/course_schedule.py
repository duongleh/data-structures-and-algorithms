# https://leetcode.com/problems/course-schedule
# O(V+E) T | O(V) S

from graph import AdjacencyListGraph
from detect_cycle_in_directed_graph import detect_cycle_in_directed_graph


def schedule_course(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = AdjacencyListGraph(is_directed=True)
    for end_course, start_course in prerequisites:
        graph.add_edge(start_course, end_course)

    visited = set()
    for start_course in range(num_courses):
        if detect_cycle_in_directed_graph(graph, start_course, visited, []):
            return False
    return True
