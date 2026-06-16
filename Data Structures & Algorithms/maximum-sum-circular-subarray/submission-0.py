class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadanesMax(nums):
            max_sum = nums[0]
            current_sum = nums[0]
            for i in range(1, len(nums)):
                current_sum = max(nums[i], current_sum + nums[i])
                max_sum = max(current_sum, max_sum)
            return max_sum

        def kadanesMin(nums):
            min_sum = nums[0]
            current_sum = nums[0]
            for i in range(1, len(nums)):
                current_sum = min(nums[i], current_sum + nums[i])
                min_sum = min(min_sum, current_sum)
            return min_sum

        # Scenario A
        max_sum = kadanesMax(nums)

        # scenario B
        total = sum(nums)
        min_sum = kadanesMin(nums)

        max_subarray = total - min_sum

        # if all are negative
        if max_sum < 0:
            return max_sum

            # Return the bigger of the two scenarios
        return max(max_sum, max_subarray)