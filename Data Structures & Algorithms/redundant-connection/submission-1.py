class DSU:
    def __init__(self, n):
        # Initially, each node is its own parent
        self.parent = list(range(n + 1))

    def find(self, i):
        # If i is its own parent, it's the captain
        if self.parent[i] == i:
            return i
        # Otherwise, keep looking up the chain
        return self.find(self.parent[i])
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u,v):
                return [u,v]


        