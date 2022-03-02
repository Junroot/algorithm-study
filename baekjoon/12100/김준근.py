from collections import deque

n = int(input())


def up(board):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for column in range(n):
        new_column = []
        numbers = []

        for index_of_numbers in range(n):
            if board[index_of_numbers][column] != 0:
                numbers.append(board[index_of_numbers][column])

        index_of_numbers = 0
        while index_of_numbers < len(numbers) - 1:
            if numbers[index_of_numbers] == numbers[index_of_numbers + 1]:
                new_column.append(numbers[index_of_numbers] * 2)
                index_of_numbers += 1
            else:
                new_column.append(numbers[index_of_numbers])
            index_of_numbers += 1

        if index_of_numbers == len(numbers) - 1:
            new_column.append(numbers[index_of_numbers])

        for i in range(len(new_column)):
            result[i][column] = new_column[i]
    return result


def down(board):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for column in range(n):
        new_column = []
        numbers = []

        for index_of_numbers in range(n):
            if board[index_of_numbers][column] != 0:
                numbers.append(board[index_of_numbers][column])

        index_of_numbers = len(numbers) - 1
        while index_of_numbers > 0:
            if numbers[index_of_numbers] == numbers[index_of_numbers - 1]:
                new_column.append(numbers[index_of_numbers] * 2)
                index_of_numbers -= 1
            else:
                new_column.append(numbers[index_of_numbers])
            index_of_numbers -= 1

        if index_of_numbers == 0:
            new_column.append(numbers[index_of_numbers])

        for i in range(len(new_column)):
            result[n - 1 - i][column] = new_column[i]
    return result


def left(board):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(n):
        new_row = []
        numbers = list(filter(lambda x: x != 0, board[row]))

        index_of_numbers = 0
        while index_of_numbers < len(numbers) - 1:
            if numbers[index_of_numbers] == numbers[index_of_numbers + 1]:
                new_row.append(numbers[index_of_numbers] * 2)
                index_of_numbers += 1
            else:
                new_row.append(numbers[index_of_numbers])
            index_of_numbers += 1

        if index_of_numbers == len(numbers) - 1:
            new_row.append(numbers[index_of_numbers])

        for i in range(len(new_row)):
            result[row][i] = new_row[i]
    return result


def right(board):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(n):
        new_row = []
        numbers = list(filter(lambda x: x != 0, board[row]))

        index_of_numbers = len(numbers) - 1
        while index_of_numbers > 0:
            if numbers[index_of_numbers] == numbers[index_of_numbers - 1]:
                new_row.append(numbers[index_of_numbers] * 2)
                index_of_numbers -= 1
            else:
                new_row.append(numbers[index_of_numbers])
            index_of_numbers -= 1

        if index_of_numbers == 0:
            new_row.append(numbers[index_of_numbers])

        for i in range(len(new_row)):
            result[row][n - 1 - i] = new_row[i]
    return result


init_board = [list(map(int, input().split())) for _ in range(n)]

queue = deque([(init_board, 0)])
result = 0


while queue:
    current_board, count = queue.popleft()
    result = max(result, max(map(max, current_board)))
    if count == 5:
        continue
    queue.append((left(current_board), count + 1))
    queue.append((up(current_board), count + 1))
    queue.append((right(current_board), count + 1))
    queue.append((down(current_board), count + 1))

print(result)

