n = int(input())

array_x = []
array_y = []

for i in range(n):
    x, y = map(int, input().split())
    array_x.append(x)
    array_y.append(y)

array_d = input()

right_min = {}
left_max = {}

for i in range(n):
    if array_d[i] == 'R':
        if array_y[i] in left_max and left_max[array_y[i]] > array_x[i]:
            print("Yes")
            exit(0)
    else:
        if array_y[i] in right_min and right_min[array_y[i]] < array_x[i]:
            print("Yes")
            exit(0)

    if array_d[i] == 'R':
        if array_y[i] not in right_min:
            right_min[array_y[i]] = array_x[i]
        else:
            right_min[array_y[i]] = min(right_min[array_y[i]], array_x[i])
    else:
        if array_y[i] not in left_max:
            left_max[array_y[i]] = array_x[i]
        else:
            left_max[array_y[i]] = max(left_max[array_y[i]], array_x[i])


print("No")
