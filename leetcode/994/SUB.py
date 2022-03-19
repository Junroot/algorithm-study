class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        length = len(grid)
        width = len(grid[0])

        queue = deque([])

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append([i, j])

        while queue:
            x, y = queue.popleft()
            minute = grid[x][y]

            if x < length - 1:
                if grid[x + 1][y] == 1:
                    grid[x + 1][y] = minute + 1
                    queue.append([x + 1, y])
            if x > 0:
                if grid[x - 1][y] == 1:
                    grid[x - 1][y] = minute + 1
                    queue.append([x - 1, y])
            if y < width - 1:
                if grid[x][y + 1] == 1:
                    grid[x][y + 1] = minute + 1
                    queue.append([x, y + 1])
            if y > 0:
                if grid[x][y - 1] == 1:
                    grid[x][y - 1] = minute + 1
                    queue.append([x, y - 1])

        ans = 0
        is_end = 1
        orage_count = 0

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    is_end = 0
                else:
                    ans = max(grid[i][j], ans)

        if is_end == 0:
            return -1
        elif ans == 0:
            return 0
        else:
            return ans - 2
