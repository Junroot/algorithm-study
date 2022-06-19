from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(board, card_positions_by_card, cards: set, r, c):
    if len(cards) == 0:
        return 0
    result = 100000
    for card in cards:
        card_positions = card_positions_by_card[card]

        result1 = get_min_input_count(board, (r, c), card_positions[0]) + 1
        result1 += get_min_input_count(board, card_positions[0], card_positions[1]) + 1
        board[card_positions[0][0]][card_positions[0][1]] = 0
        board[card_positions[1][0]][card_positions[1][1]] = 0

        result1 += solve(board, card_positions_by_card, cards.difference([card]), card_positions[1][0],
                         card_positions[1][1])
        board[card_positions[1][0]][card_positions[1][1]] = card
        board[card_positions[0][0]][card_positions[0][1]] = card

        result2 = get_min_input_count(board, (r, c), card_positions[1]) + 1
        result2 += get_min_input_count(board, card_positions[1], card_positions[0]) + 1
        board[card_positions[1][0]][card_positions[1][1]] = 0
        board[card_positions[0][0]][card_positions[0][1]] = 0
        result2 += solve(board, card_positions_by_card, cards.difference([card]), card_positions[0][0],
                         card_positions[0][1])
        board[card_positions[1][0]][card_positions[1][1]] = card
        board[card_positions[0][0]][card_positions[0][1]] = card
        result = min([result1, result2, result])

    return result


def get_min_input_count(board, start, destination):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[start[0]][start[1]] = True

    q = deque([(start[0], start[1])])
    input_count = 0
    while q:
        q_length = len(q)
        for _ in range(q_length):
            current_r, current_c = q.popleft()
            if destination[0] == current_r and destination[1] == current_c:
                return input_count
            for direction in directions:
                next_r = current_r + direction[0]
                next_c = current_c + direction[1]
                if is_valid_position(next_r, next_c) and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))
                next_r, next_c = move_with_ctrl(current_r, current_c, direction, board)
                if not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))
        input_count += 1


def is_valid_position(r, c):
    return 0 <= r < 4 and 0 <= c < 4


def move_with_ctrl(r, c, direction, board):
    while True:
        next_r = r + direction[0]
        next_c = c + direction[1]
        if not is_valid_position(next_r, next_c):
            return r, c
        if board[next_r][next_c] != 0:
            return next_r, next_c
        r = next_r
        c = next_c


def solution(board, r, c):
    card_positions = dict()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card = board[i][j]
                if card not in card_positions:
                    card_positions[card] = [(i, j)]
                else:
                    card_positions[card].append((i, j))
    return solve(board, card_positions, set(card_positions.keys()), r, c)


print(solution([[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 1, 0))
