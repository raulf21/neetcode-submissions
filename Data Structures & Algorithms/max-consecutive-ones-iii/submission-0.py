class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        longest = 0
        zeros = 0
        for R in range(len(nums)):
            # expand the window
            if nums[R] == 0:
                zeros +=1

            while zeros > k:
                if nums[L] == 0:
                    zeros -=1
                L +=1
            longest = max(longest, R - L + 1)
        return longest


        