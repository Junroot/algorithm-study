n = int(input())
arr = list(map(int, list(input().split())))
dic = dict()
dic[arr[0]] = 1
ans = 0

for i in range(n):
    max_len = 0

    for j in range(0, i):
        if dic[arr[j]] > max_len and arr[i] > arr[j]:
            max_len = dic[arr[j]]

    dic[arr[i]] = max_len + 1
    if dic[arr[i]] > ans:
        ans = dic[arr[i]]

print(ans)