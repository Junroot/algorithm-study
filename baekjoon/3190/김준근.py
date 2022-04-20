from collections import deque

board_size = int(input())
apple_count = int(input())
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
turns = dict()

for _ in range(apple_count):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

turn_count = int(input())
for _ in range(turn_count):
    time, direction = input().split()
    time = int(time)
    turns[time] = direction

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

time = 0
snake_body = deque([(0, 0)])
board[0][0] = 2
snake_direction_index = 0

while snake_body:
    head = snake_body[0]

    snake_direction = directions[snake_direction_index]
    next_head = (head[0] + snake_direction[0], head[1] + snake_direction[1])

    if next_head[0] < 0 or next_head[0] >= board_size or next_head[1] < 0 or next_head[1] >= board_size:
        break
    if board[next_head[1]][next_head[0]] == 2:
        break

    snake_body.appendleft(next_head)

    if board[next_head[1]][next_head[0]] == 0:
        tail = snake_body.pop()
        board[tail[1]][tail[0]] = 0
    board[next_head[1]][next_head[0]] = 2
    time += 1
    if time in turns:
        if turns[time] == "D":
            snake_direction_index = (snake_direction_index + 1) % len(directions)
        else:
            snake_direction_index = (snake_direction_index - 1 + len(directions)) % len(directions)

print(time + 1)
