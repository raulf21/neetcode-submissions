class DSU:
    def __init__(self,nums):
        self.parents = {n:n for n in nums}
        self.size = {n: 1 for n in nums}
        self.max_size = 1 if nums else 0

    def find(self, i):
        if self.parents[i] == i:
            return i

        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Standard Union: make root_i the parent of root_j
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            
            self.parents[root_j] = root_i
            # New Step: Transfer the size of the smaller group to the larger one
            self.size[root_i] += self.size[root_j]
            
            # Keep track of the global maximum size
            self.max_size = max(self.max_size, self.size[root_i])

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        dsu = DSU(num_set)
        for n in num_set:
            if (n+1) in num_set:
                dsu.union(n, n+1)
        return dsu.max_size