board_length, spell_count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(board_length)]
spells = [tuple(map(int, input().split())) for _ in range(spell_count)]
directions = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
shark_position = (board_length // 2, board_length // 2)
result = 0


def blizzard(direction_index):
    global direction
    direction = directions[direction_index]
    for i in range(1, distance + 1):
        new_x = shark_position[0] + direction[0] * i
        new_y = shark_position[1] + direction[1] * i
        board[new_y][new_x] = 0


def next_position(x, y):
    relative_direction = (0, 1)
    if board_length - y - 1 <= x < y:
        relative_direction = (1, 0)
    elif board_length - x <= y <= x:
        relative_direction = (0, -1)
    elif y <= x <= board_length - y - 1:
        relative_direction = (-1, 0)
    return x + relative_direction[0], y + relative_direction[1]


def explode_balls():
    global result, board
    is_exploded = True
    while is_exploded:
        is_exploded = False
        new_board = [[0 for _ in range(board_length)] for _ in range(board_length)]
        last_position = (shark_position[0] - 1, shark_position[1])
        position = (shark_position[0] - 1, shark_position[1])
        ball_group = -1
        group_length = 0
        while position != (-1, 0):
            if board[position[1]][position[0]] == 0:
                position = next_position(position[0], position[1])
                continue
            elif board[position[1]][position[0]] != ball_group:
                if group_length < 4:
                    for _ in range(group_length):
                        new_board[last_position[1]][last_position[0]] = ball_group
                        last_position = next_position(last_position[0], last_position[1])
                else:
                    result += ball_group * group_length
                    is_exploded = True
                ball_group = board[position[1]][position[0]]
                group_length = 1
            else:
                group_length += 1

            position = next_position(position[0], position[1])
        if group_length < 4:
            for _ in range(group_length):
                new_board[last_position[1]][last_position[0]] = ball_group
                last_position = next_position(last_position[0], last_position[1])
        else:
            is_exploded = True
            result += ball_group * group_length
        board = new_board


def update_balls():
    global board
    last_position = (shark_position[0] - 1, shark_position[1])
    position = (shark_position[0] - 1, shark_position[1])
    ball_group = -1
    group_length = 0
    new_board = [[0 for _ in range(board_length)] for _ in range(board_length)]
    while position != (-1, 0):
        if board[position[1]][position[0]] == 0:
            position = next_position(position[0], position[1])
            continue
        elif board[position[1]][position[0]] != ball_group:
            if group_length != 0:
                new_board[last_position[1]][last_position[0]] = group_length
                last_position = next_position(last_position[0], last_position[1])
                if last_position == (-1, 0):
                    break
                new_board[last_position[1]][last_position[0]] = ball_group
                last_position = next_position(last_position[0], last_position[1])
                if last_position == (-1, 0):
                    break
            ball_group = board[position[1]][position[0]]
            group_length = 1
        else:
            group_length += 1

        position = next_position(position[0], position[1])

    if group_length != 0:
        if last_position != (-1, 0):
            new_board[last_position[1]][last_position[0]] = group_length
            last_position = next_position(last_position[0], last_position[1])

        if last_position != (-1, 0):
            new_board[last_position[1]][last_position[0]] = ball_group

    board = new_board


for direction_index, distance in spells:
    blizzard(direction_index)
    explode_balls()
    update_balls()


print(result)
