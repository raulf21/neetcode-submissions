class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1 # points to where the next unique element goes
        for read in range(1, len(nums)):
            if nums[read-1] != nums[read]:
                # unique number found
                nums[write] = nums[read] # Overwrite the duplicate
                write +=1
        return write
        