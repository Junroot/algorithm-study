import collections
import bisect


def longestPath(self, A: list[int], s: str) -> int:
    n = len(A)
    child_num = [0] * n

    for a in A[1:]:
        child_num[a] += 1

    longest = [[0] for _ in range(n)]

    dq = collections.deque()
    for i in range(n):
        if child_num[i] == 0:
            dq.append([i, 1])

    ans = 1
    while dq:
        cur_i, cur_l = dq.popleft()
        cur_p = A[cur_i]

        child_num[cur_p] -= 1

        if s[cur_p] != s[cur_i]:
            bisect.insort_right(longest[cur_p], cur_l)
            if len(longest[cur_p]) > 2:
                longest[cur_p].pop(0)

        if child_num[cur_p] == 0:
            ans = max(ans, 1 + sum(longest[cur_p][-2:]))
            dq.append([cur_p, 1 + longest[cur_p][-1]])

    return ans
