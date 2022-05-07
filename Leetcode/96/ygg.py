def numTrees(n: int) -> int:
    if n == 1:
        return 1

    ans = [0] * (n + 1)
    ans[0] = 1
    ans[1] = 1
    ans[2] = 2

    for i in range(3, n+1):
        for j in range(i):
            ans[i] += ans[j] * ans[i-1-j]

    return ans[n]


print(numTrees(3))
print(numTrees(10))
