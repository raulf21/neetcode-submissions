class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            # include decision
            subset.append(nums[i])
            backtrack(i+1, subset)

            # dont include in decision
            subset.pop()
            backtrack(i+1, subset)

        backtrack(0, [])
        return res