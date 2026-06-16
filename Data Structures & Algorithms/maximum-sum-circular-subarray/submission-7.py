class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, maxSum = nums[0], nums[0]
        curMin, minSum = nums[0], nums[0]
        total = sum(nums)

        for i in range(1,len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(curMax, maxSum)

            # update min
            curMin = min(nums[i], curMin + nums[i])
            minSum = min(curMin, minSum)

        if total == minSum:
            return maxSum
        
        return max(maxSum, total - minSum)
        