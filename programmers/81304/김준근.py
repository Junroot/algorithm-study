import heapq


def solution(n, start, end, roads, traps):
    maze = [[] for _ in range(n + 1)]
    reversed_maze = [[] for _ in range(n + 1)]
    trap_ids = {node: i for i, node in enumerate(traps)}

    for p, q, s in roads:
        maze[p].append((q, s))
        reversed_maze[q].append((p, s))

    maze_visited = set()

    pq = [(0, start, 0)]
    while pq:
        current_distance, node, active_bit = heapq.heappop(pq)
        if node == end:
            return current_distance
        if (node, active_bit) in maze_visited:
            continue

        maze_visited.add((node, active_bit))

        for next_node, weight in maze[node]:
            active_count = 0
            if node in trap_ids and (active_bit >> trap_ids[node]) & 1 > 0:
                active_count += 1
            if next_node in trap_ids and (active_bit >> trap_ids[next_node]) & 1 > 0:
                active_count += 1

            if next_node in trap_ids:
                if active_bit >> trap_ids[next_node] & 1 > 0:
                    next_active_bit = active_bit ^ (1 << trap_ids[next_node])
                else:
                    next_active_bit = active_bit | (1 << trap_ids[next_node])
            else:
                next_active_bit = active_bit

            if active_count % 2 == 0 and (next_node, next_active_bit) not in maze_visited:
                heapq.heappush(pq, (current_distance + weight, next_node, next_active_bit))

        for next_node, weight in reversed_maze[node]:
            active_count = 0
            if node in trap_ids and (active_bit >> trap_ids[node]) & 1 > 0:
                active_count += 1
            if next_node in trap_ids and (active_bit >> trap_ids[next_node]) & 1 > 0:
                active_count += 1

            if next_node in trap_ids:
                if active_bit >> trap_ids[next_node] & 1 > 0:
                    next_active_bit = active_bit ^ (1 << trap_ids[next_node])
                else:
                    next_active_bit = active_bit | (1 << trap_ids[next_node])
            else:
                next_active_bit = active_bit

            if active_count % 2 == 1 and (next_node, next_active_bit) not in maze_visited:
                heapq.heappush(pq, (current_distance + weight, next_node, next_active_bit))

    return -1


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
