class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)

        for r in range(len(nums)):
            rightSum = total - leftSum - nums[r]
            if rightSum == leftSum:
                return r
            leftSum += nums[r]
        return -1
        