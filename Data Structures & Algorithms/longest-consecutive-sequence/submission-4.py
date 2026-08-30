class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        longest = 0
        for num in sequence:
            # Only start if 'num' is absolute beginning
            if num - 1 not in sequence:
                current_num = num
                current_streak = 1

                while current_num + 1 in sequence:
                    current_num +=1
                    current_streak +=1

                longest = max(longest, current_streak)
        return longest

        