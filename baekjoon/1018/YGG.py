def paint_area(m: int, n: int, arr) -> int:
    count = 0
    start = 0 + 0
    char = arr[0][0]
    for i in range(8):
        for j in range(8):
            if ((i + j) % 2 == start % 2) ^ (arr[i][j] == char):
                count += 1
    prev_val = count
    ans = min(count, 64 - count)

    for y in range(0, len(arr) - 8):
        # (0~n-8, 0~7) -> (8~n-1, 0~7)
        start = y + 0
        for x in range(8):
            if ((y + x) % 2 == 0) ^ (arr[y][x] == char):
                count -= 1
            if ((y+8 + x) % 2 == 0) ^ (arr[y+8][x] == char):
                count += 1
        ans = min(ans, count, 64 - count)

    for j in range(0, len(arr[0]) - 8):
        count = prev_val
        # (0~7, j-8) -> (0~7, j)
        start = 0 + j+1
        for y in range(8):
            if ((y + j) % 2 == 0) ^ (arr[y][j] == char):
                count -= 1
            if ((y + j+8) % 2 == 0) ^ (arr[y][j+8] == char):
                count += 1
        prev_val = count
        ans = min(ans, count, 64 - count)

        j += 1
        for y in range(0, len(arr) - 8):
            start = y + j
            # (0~n-8, j~j+7) -> (8~n-1, j~j+7)
            for x in range(8):
                if ((y + j+x) % 2 == 0) ^ (arr[y][j+x] == char):
                    count -= 1
                if ((y+8 + j+x) % 2 == 0) ^ (arr[y+8][j+x] == char):
                    count += 1
            ans = min(ans, count, 64 - count)

    return ans


a, b = map(int, input().split())
arr = []
for k in range(a):
    arr.append(input())

print(paint_area(a, b, arr))