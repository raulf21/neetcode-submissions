class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        res = curSum =  0

        for num in nums:
            curSum += num
            diff = curSum - k

            res += hashMap.get(diff, 0)
            hashMap[curSum] = 1 + hashMap.get(curSum, 0)
        return res
            
        