
import heapq

def heuristic(state, goal):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

def successors(state):
    i = state.index(0)
    moves = []
    for j in [i-3, i+3, i-1, i+1]:
        if 0 <= j < 9:
            if abs(i//3 - j//3) + abs(i%3 - j%3) == 1:
                new_state = list(state)
                new_state[i], new_state[j] = new_state[j], new_state[i]
                moves.append(tuple(new_state))
    return moves

def best_first(start, goal):
    pq = [(heuristic(start, goal), start)]
    visited = set()
    parent = {start: None}

    while pq:
        h, state = heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in successors(state):
            if nxt not in visited and nxt not in parent:
                parent[nxt] = state
                heapq.heappush(pq, (heuristic(nxt, goal), nxt))

    return None

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path = best_first(start, goal)
if path:
    for state in path:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution found")
