n, k = map(int, input().split())

cards = list(map(int, input().split()))
dic = dict()
arr = []

for i in range(len(cards)):
    cur = cards[i]

    if len(arr) == 0 or arr[-1][-1] < cur:
        arr.append([cur])
        if len(arr[-1]) >= k:
            for e in arr[-1]:
                dic[e] = i + 1
            del arr[-1]
    elif cur < arr[0][-1]:
        arr[0].append(cur)
        if len(arr[0]) >= k:
            for e in arr[0]:
                dic[e] = i + 1
            del arr[0]
    else:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid][-1] < cur < arr[mid+1][-1]:
                arr[mid+1].append(cur)

                if len(arr[mid+1]) >= k:
                    for e in arr[mid+1]:
                        dic[e] = i + 1
                    del arr[mid+1]
                    break
            elif arr[mid + 1][-1] < cur:
                start = mid + 1
            else:
                end = mid - 1

for i in range(1, n+1):
    if i not in dic:
        print(-1)
    else:
        print(dic[i])