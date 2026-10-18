colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color = {}

def is_valid(node, c):
    for neighbour in graph[node]:
        if neighbour in color and color[neighbour] == c:
            return False
    return True

def solve(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for c in colors:
        if is_valid(region, c):
            color[region] = c

            if solve(node + 1):
                return True

            del color[region]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for region in color:
        print(region, ":", color[region])
else:
    print("No solution exists")
