import copy


def solution(board, aloc, bloc):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def find_optimal_movement(board, my_loc, opposite_loc):
        if board[my_loc[0]][my_loc[1]] == 0:
            return False, 0

        next_locations = []
        for direction in directions:
            next_location = [my_loc[0] + direction[0], my_loc[1] + direction[1]]
            if 0 <= next_location[0] < len(board) and 0 <= next_location[1] < len(board[0]) \
                    and board[next_location[0]][next_location[1]] == 1:
                next_locations.append(next_location)

        if len(next_locations) == 0:
            return False, 0

        win_movements = []
        lose_movements = []
        for next_location in next_locations:
            next_board = copy.deepcopy(board)
            next_board[my_loc[0]][my_loc[1]] = 0
            is_opposite_win, move_count = find_optimal_movement(next_board, opposite_loc, next_location)
            if not is_opposite_win:
                win_movements.append(move_count + 1)
            else:
                lose_movements.append(move_count + 1)

        if len(win_movements) > 0:
            return True, min(win_movements)
        return False, max(lose_movements)

    return find_optimal_movement(board, aloc, bloc)[1]


print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
