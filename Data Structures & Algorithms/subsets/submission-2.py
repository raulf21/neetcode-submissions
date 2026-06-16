class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curset = [], []

        def dfs(i):
            if i>=len(nums):
                res.append(curset.copy())
                return 
            curset.append(nums[i])
            dfs(i+1)
            curset.pop()
            dfs(i+1)
        dfs(0)

        return res
        