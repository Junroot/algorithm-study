from collections import deque

MIN_POSITION = 0
MAX_POSITION = 100000


movements = [lambda x: x + 1, lambda x: x - 1, lambda x: x * 2]
n, k = map(int, input().split())

visited = {n}
q = deque([(n, 0)])

while q:
    position, time = q.popleft()
    if position == k:
        print(time)
        break
    for movement in movements:
        new_position = movement(position)
        if MIN_POSITION <= new_position <= MAX_POSITION and new_position not in visited:
            visited.add(new_position)
            q.append((new_position, time + 1))
