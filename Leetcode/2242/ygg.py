import heapq

def maximumScore(scores: list[int], edges: list[list[int]]) -> int:
    ans = -1

    nodes = [[] for n in range(len(scores))]
    for e in edges:
        nodes[e[0]].append([scores[e[1]], e[1]])
        nodes[e[1]].append([scores[e[0]], e[0]])
    for i in range(len(nodes)):
        nodes[i] = heapq.nlargest(3, nodes[i])

    for i, j in edges:
        for vx, x in nodes[i]:
            for vy, y in nodes[j]:
                if x != y and x != j and y != i:
                    ans = max(ans, vx + vy + scores[i] + scores[j])

    return ans


print(maximumScore([5,2,9,8,4], [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(maximumScore([9,20,6,4,11,12], [[0,3],[5,3],[2,4],[1,3]]))
print(maximumScore([16,21,22,2,24,21,12,17,2,24], [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,0]]))
