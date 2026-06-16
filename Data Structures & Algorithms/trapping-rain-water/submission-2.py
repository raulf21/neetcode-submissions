class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftSum, rightSum = height[l], height[r]
        res = 0
        while l<r:
            if leftSum < rightSum: 
                l +=1
                leftSum = max(leftSum, height[l])
                res += leftSum - height[l]
            else:
                r -=1
                rightSum = max(rightSum, height[r])
                res += rightSum - height[r]
        return res
        