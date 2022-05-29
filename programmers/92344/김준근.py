def solution(board, skill):
    height = len(board)
    width = len(board[0])

    difference_board = [[0 for _ in range(width)] for _ in range(height)]

    for s in skill:
        type, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
        if type == 1:
            degree *= -1

        difference_board[r1][c1] += degree
        if r2 + 1 < height:
            difference_board[r2 + 1][c1] -= degree
        if c2 + 1 < width:
            difference_board[r1][c2 + 1] -= degree
        if c2 + 1 < width and r2 + 1 < height:
            difference_board[r2 + 1][c2 + 1] += degree

    answer = 0

    for i in range(1, height):
        for j in range(width):
            difference_board[i][j] += difference_board[i - 1][j]

    for i in range(1, width):
        for j in range(height):
            difference_board[j][i] += difference_board[j][i - 1]

    for i in range(height):
        for j in range(width):
            if board[i][j] + difference_board[i][j] > 0:
                answer += 1
    return answer

