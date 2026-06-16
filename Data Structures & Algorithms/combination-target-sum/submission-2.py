class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current_target, path):
            if i == len(nums) or current_target < 0:
                return
            if current_target == 0:
                res.append(path.copy())
                return 
            
            # Include the same index
            path.append(nums[i])
            backtrack(i, current_target-nums[i], path)
            # dont include it
            path.pop()
            backtrack(i+1, current_target, path)
        backtrack(0, target, [])

        return res