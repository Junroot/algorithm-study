class Union_find:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.group = n
        
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.group -= 1
    
    def count(self) -> int:
        return self.group

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        str_map = collections.defaultdict(int)
        for i, s in enumerate(strs):
            str_map[s] = i
        
        n, length = len(strs), len(strs[0])
        uf = Union_find(n)
        for i in range(n):
            for j in range(i+1, n):
                unmatched = 0
                is_union = True
                for k in range(length):
                    if strs[i][k] != strs[j][k]:
                        unmatched += 1
                    if unmatched > 2:
                        is_union = False
                        break
                if is_union:
                    uf.union(i, j)
        
        return uf.count()
