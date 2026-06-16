class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res = max(res,total)
            if total < 0:
                total = 0
        return res
        
        