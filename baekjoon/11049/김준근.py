from sys import stdin

n = int(input())
matrix_sizes = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

cache = [[0 for _ in range(n)] for _ in range(n)]

for size in range(1, n):
    for start in range(n - size):
        end = start + size
        cache[start][end] = 2**31
        for mid in range(start, end):
            left_count = cache[start][mid]
            right_count = cache[mid + 1][end]
            multiplication_count = matrix_sizes[start][0] * matrix_sizes[mid][1] * matrix_sizes[end][1]
            cache[start][end] = min(cache[start][end], left_count + right_count + multiplication_count)

print(cache[0][n - 1])
