n, m = map(int, input().split())
arr = []
house = []
chicken = []
ans = 1000000

for _ in range(n):
    arr.append(list(map(int, list(input().split()))))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([j, i])
        if arr[i][j] == 2:
            chicken.append([j, i])

m = len(chicken) - m


def count_chicken():
    total = 0
    global ans

    for i in range(len(house)):
        chicken_min = 10000
        for j in range(len(chicken)):
            if chicken_min > abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1]):
                chicken_min = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
        total+=chicken_min

    if total < ans:
        ans = total


def delete_chicken(num, index):
    if num == m:
        count_chicken()
        return

    for i in range(index, len(chicken)):
        chicken_x, chicken_y = chicken[i]
        chicken.pop(i)
        delete_chicken(num+1, i)
        chicken.insert(i, [chicken_x, chicken_y])


delete_chicken(0, 0)
print(ans)