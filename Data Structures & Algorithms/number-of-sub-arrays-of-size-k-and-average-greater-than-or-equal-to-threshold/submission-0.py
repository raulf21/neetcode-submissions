class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = 0
        L = 0
        targetSum = k * threshold
        for R in range(len(arr)):
            curSum += arr[R]
            if R - L + 1 > k:
                curSum -= arr[L]
                L += 1
            
            if R - L + 1 == k and curSum >= targetSum:
                res += 1

        return res