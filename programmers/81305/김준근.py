import sys

sys.setrecursionlimit(10000000)

INF = 987654312


def solution(k, num, links):
    has_parent = [False for _ in range(len(num))]
    for children in links:
        for child in children:
            if child != -1:
                has_parent[child] = True

    root = 0
    for i, p in enumerate(has_parent):
        if not p:
            root = i
            break

    max_result = sum(num) + 1
    min_result = max(1, sum(num) // k)

    def count_group(group_size, root_node):
        if root_node == -1:
            return 1, 0
        if num[root_node] > group_size:
            return INF, INF
        left_group_count, left_group_root_size = count_group(group_size, links[root_node][0])
        right_group_count, right_group_root_size = count_group(group_size, links[root_node][1])

        if left_group_root_size + right_group_root_size + num[root_node] <= group_size:
            return left_group_count + right_group_count - 1, left_group_root_size + right_group_root_size + num[
                root_node]
        min_group_size = min(left_group_root_size, right_group_root_size)
        if min_group_size + num[root_node] <= group_size:
            return left_group_count + right_group_count, min_group_size + num[root_node]

        return left_group_count + right_group_count + 1, num[root_node]

    while min_result < max_result:
        mid = (min_result + max_result) // 2
        group_count, group_root_size = count_group(mid, root)
        if group_count > k:
            min_result = mid + 1
        else:
            max_result = mid

    return min_result


print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
