
def dls(graph, node, goal, limit):
    if node == goal:
        return [node]

    if limit == 0:
        return None

    for child in graph.get(node, []):
        path = dls(graph, child, goal, limit - 1)
        if path:
            return [node] + path

    return None

def ids(graph, start, goal):
    depth = 0

    while True:
        result = dls(graph, start, goal, depth)
        if result:
            return result
        depth += 1

graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    children = input("Enter children separated by spaces: ").split()
    graph[node] = children

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = ids(graph, start, goal)
print("Path:", path)
