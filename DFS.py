g = {
    "A": ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbor in graph[root]:
            dfs(visited, graph, neighbor)

# Example usage:
visited = set()
dfs(visited, g, 'A')
