class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            # if our current candidate has been fully canceled out, 
            # we nominate the current number as the new candidate
            if count == 0:
                candidate = num

            # If we see our candidate again, they gain power (+1)
            # Otherwise, an opponnent cancels them out (-1)
            if num == candidate:
                count +=1
            else:
                count -=1
        return candidate
        