graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

h = {'A': 6, 'B': 4, 'C': 4, 'D': 3, 'E': 2, 'F': 0}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if node not in visited:
            visited.add(node)

            for neighbour, cost in graph[node]:
                if neighbour not in visited:
                    new_g = g + cost
                    new_f = new_g + h[neighbour]
                    open_list.append((new_f, new_g, neighbour, path + [neighbour]))

    print("No path found")

astar('A', 'F')
