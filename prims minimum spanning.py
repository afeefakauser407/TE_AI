import sys

def prims(graph):
    num_vertices = len(graph)
    mst = []  # Minimum Spanning Tree
    visited = [False] * num_vertices
    min_weights = [float('inf')] * num_vertices
    min_weights[0] = 0  # Start from the first vertex

    for _ in range(num_vertices):
        # Find the vertex with the minimum weight that is not yet in the MST
        min_weight = float('inf')
        min_vertex = -1
        for v in range(num_vertices):
            if not visited[v] and min_weights[v] < min_weight:
                min_weight = min_weights[v]
                min_vertex = v

        if min_vertex == -1:
            break

        visited[min_vertex] = True
        mst.append(min_vertex)

        # Update the minimum weights of the adjacent vertices
        for neighbor, weight in graph[min_vertex]:
            if not visited[neighbor] and weight < min_weights[neighbor]:
                min_weights[neighbor] = weight

    return mst

# Example usage:
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 1), (3, 1)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 1), (2, 4)]
}

mst = prims(graph)
print("Minimum Spanning Tree:", mst)
