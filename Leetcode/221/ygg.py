# brute force

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        maxlen = 0
        for y in range(row):
            for x in range(col):
                if matrix[y][x] == "1" and y + maxlen < row and x + maxlen < col:
                    # print(y, x, matrix[y][x])
                    i, j = y + maxlen, x + maxlen
                    if matrix[i][j] != "0":
                        filled = True
                        for m in range(y, i):
                            for n in range(x, j):
                                if matrix[m][n] == "0":
                                    filled = False
                                    break
                            if not filled:
                                break
                        if not filled:
                            continue

                    while i < row and j < col and matrix[i][j] == "1":
                        if matrix[i][j] == "1":
                            filled = True
                            for m in range(y, i):
                                if matrix[m][j] == "0":
                                    filled = False
                                    break
                            for n in range(x, j):
                                if matrix[i][n] == "0":
                                    filled = False
                                    break
                            if not filled:
                                break
                        else:
                            break

                        i += 1
                        j += 1

                    # print(y, x, i, j)
                    maxlen = max(maxlen, i - y)

        return maxlen * maxlen


# dp

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [list(map(int, m)) for m in matrix]

        ans = max(dp[0])
        for y in range(0, len(dp)):
            if dp[y][0] == 1:
                ans = 1

        for y in range(1, len(dp)):
            for x in range(1, len(dp[0])):
                if dp[y][x] == 1:
                    dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
                    if dp[y][x] > ans:
                        ans = dp[y][x]

        return ans ** 2
