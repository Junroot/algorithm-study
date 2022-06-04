n = int(input())

arr = [0] * n
ans = 0

def nqueen(row):
    global ans
    if row == n:
        ans+=1
        return

    for i in range(n):
        arr[row] = i

        check = 1
        if row > 0:
            for j in range(row):
                if arr[j] == arr[row] or abs(arr[j] - arr[row]) == abs(j-row):
                    check = 0
                    break

        if check == 1:
            nqueen(row+1)

nqueen(0)
print(ans)