import heapq

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}  # Initialize distances with infinity
    distances[source] = 0  # Distance from source to itself is 0
    queue = [(0, source)]  # Priority queue of (distance, vertex)

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue  # Skip if we've found a better distance for this vertex

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2}
}

source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from", source_vertex + ":")
for vertex, distance in shortest_distances.items():
    print(vertex, "->", distance)
