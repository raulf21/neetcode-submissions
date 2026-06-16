class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        totalArea = 0

        while l<r:
            totalArea = max(totalArea, (r-l) * (min(heights[l], heights[r])))
            if heights[l] < heights[r]:
                l +=1
            else:
                r-=1
        return totalArea
        