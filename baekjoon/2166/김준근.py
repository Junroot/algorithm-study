from sys import stdin

point_count = int(stdin.readline())
points = [tuple(map(int, stdin.readline().split())) for _ in range(point_count)]

point0 = points[0]
result = 0.0


def get_triangle_area(point0, point1, point2):
    a = (point1[0] - point0[0], point1[1] - point0[1])
    b = (point2[0] - point0[0], point2[1] - point0[1])
    return (a[0] * b[1] - a[1] * b[0]) * 0.5


for i in range(point_count - 1):
    point1 = points[i]
    point2 = points[i + 1]
    result += get_triangle_area(point0, point1, point2)

print(round(abs(result), 1))
