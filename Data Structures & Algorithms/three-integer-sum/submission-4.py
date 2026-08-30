class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                triplet = a + nums[left] + nums[right]

                # check if triplet to big
                if triplet > 0:
                    right -=1
                elif triplet < 0:
                    left +=1
                else:
                    result.append([a, nums[left], nums[right]])
                    left +=1
                    while left<right and nums[left] == nums[left -1]:
                        left+=1
        return result
