class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        n = len(nums)

        for i in range(n):
            # if the current element is greater than the next 
            if nums[i] > nums[(i+1) % n]:
                drops +=1
            
            # Optimization: If we find more than 1 drop, we stop
            if drops > 1:
                return False
        return True
        