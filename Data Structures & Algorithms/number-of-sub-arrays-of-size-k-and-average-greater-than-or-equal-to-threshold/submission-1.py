class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i]  + arr[i]
        

        res = l = 0
        for r in range(k - 1, len(arr)):
            sum_ = prefix[r+1] - prefix[l]
            if sum_ / k >= threshold:
                res +=1
            l +=1
        return res
