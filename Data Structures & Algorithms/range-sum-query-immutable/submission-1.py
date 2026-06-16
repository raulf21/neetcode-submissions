class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix = [0] * (n + 1)

        for i in range(len(nums)):
            self.prefix[i+1] = nums[i] + self.prefix[i]


    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix[left]
        rightSum = self.prefix[right+1]
        return rightSum - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)