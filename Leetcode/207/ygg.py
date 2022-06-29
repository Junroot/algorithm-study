class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        count = [0] * numCourses
        for n in range(numCourses):
            graph.append([])
            
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            count[pre[0]] += 1
        
        que = []
        for i in range(numCourses):
            if count[i] == 0:
                que.append(i)
        
        while que:
            n = que.pop(0)
            for i in graph[n]:
                count[i] -= 1
                if count[i] == 0:
                    que.append(i)
        
        for c in count:
            if c > 0:
                return False
        return True
            
        
#         parent = [-1] * numCourses
        
#         for pre in prerequisites:
#             if pre[0] == pre[1]: # [a, a]
#                 return False
#             if parent[pre[1]] == pre[0]:
#                 return False
#             cur = pre[1]
#             while parent[cur] != -1:
#                 cur = parent[cur]
#             if cur == pre[0]: # [[1,0],[0,2],[2,1]]
#                 return False
#             parent[pre[0]] = cur
        
#         #print(parent)
#         return True
            
