class Solution:
    def binarySearch(self, l, r, nums, target):
        if l > r:
            return -1
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binarySearch(m+1, r, nums, target)
        else:
            return self.binarySearch(l, m-1, nums, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)