class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]      # Best sum found so far
        current_sum = nums[0]  # Best sum ending at current position
        
        for i in range(1, len(nums)):
            # Decision: start fresh OR extend current subarray
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update best sum if current is better
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        