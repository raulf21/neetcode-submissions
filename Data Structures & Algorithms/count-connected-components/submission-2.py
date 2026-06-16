class DSU:
    def __init__(self, n):
        # Every node starts as its own parent
        self.parents = list(range(n))
        # rank start at 0 (inital height of trees)
        self.rank = [0] * n
        # Initally, there seperate n components
        self.count = n

    def find(self, i):
        if self.parents[i] == i:
            return i
        # Path Compression: Flatten the tree for next time
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 == root2:
            return False

        # Union by Rank: attack the shorter tree to the taller one
        if self.rank[root1] > self.rank[root2]:
            self.parents[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parents[root1] = root2
        else:
            # Rank are equal; pick one as parent and increment its rank
            self.parents[root1] = root2
            self.rank[root2] += 1
        self.count -=1 
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u,v)
        
        return dsu.count
        