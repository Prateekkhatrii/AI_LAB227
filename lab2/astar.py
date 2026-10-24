
import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)

        if g != cost[node]:
            continue

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], g

        for child, edge_cost in graph.get(node, []):
            new_g = g + edge_cost

            if child not in cost or new_g < cost[child]:
                cost[child] = new_g
                parent[child] = node
                new_f = new_g + heuristic[child]
                heapq.heappush(pq, (new_f, new_g, child))

    return None, float('inf')

graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 5, 'A': 3, 'B': 4,
    'C': 2, 'D': 6, 'G': 0
}

path, cost = a_star(graph, heuristic, 'S', 'G')
print("Path:", path)
print("Cost:", cost)
