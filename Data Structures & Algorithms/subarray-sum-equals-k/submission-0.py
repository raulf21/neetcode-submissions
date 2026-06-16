class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefix = {0 : 1}


        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefix.get(diff, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)
        return res
        