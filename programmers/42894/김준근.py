from collections import deque, defaultdict

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_areas_by_block(board, y, x):
    block_id = board[y][x]
    queue = deque([(x, y)])
    min_x, max_x = 51, -1
    min_y, max_y = 51, -1
    visited = set()
    visited.add((x, y))
    while queue:
        current_x, current_y = queue.popleft()
        min_x = min(min_x, current_x)
        max_x = max(max_x, current_x)
        min_y = min(min_y, current_y)
        max_y = max(max_y, current_y)
        for direction in directions:
            next_x = current_x + direction[0]
            next_y = current_y + direction[1]
            if 0 <= next_x < len(board[0]) and 0 <= next_y < len(board):
                if board[next_y][next_x] == block_id and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
    all_set = set()
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            all_set.add((j, i))
    return all_set


def get_areas(board):
    positions_by_block_id = dict()
    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0 and board[i][j] not in visited:
                block_id = board[i][j]
                visited.add(block_id)
                all_set = get_areas_by_block(board, i, j)
                positions_by_block_id[block_id] = all_set
    return positions_by_block_id


def fill_from(x, y, board):
    while y < len(board) and board[y][x] <= 0:
        board[y][x] = -1
        y += 1


def is_completed(board, positions_by_block_id, block_id):
    minus_count = 0
    block_count = 0
    for positions in positions_by_block_id[block_id]:
        if board[positions[1]][positions[0]] == -1:
            minus_count += 1
        if board[positions[1]][positions[0]] == block_id:
            block_count += 1
    return minus_count == 2 and block_count == 4


def solution(board):
    positions_by_block_id = get_areas(board)
    result = 0
    for i in range(len(board[0])):
        fill_from(i, 0, board)

    is_continued = True
    while is_continued:
        is_continued = False
        for block_id in positions_by_block_id.keys():
            if is_completed(board, positions_by_block_id, block_id):
                result += 1
                is_continued = True
                min_x, max_x = 51, -1
                for position in positions_by_block_id[block_id]:
                    min_x = min(min_x, position[0])
                    max_x = max(max_x, position[0])
                    board[position[1]][position[0]] = 0
                for x in range(min_x, max_x + 1):
                    fill_from(x, 0, board)

    return result


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
