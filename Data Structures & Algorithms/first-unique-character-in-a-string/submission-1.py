class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Fixed array of size 26 to hold counts for 'a' through 'z'
        count = [0] * 26
        # count frequencies using ASCII math
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Find the character in the original string with count of 1
        for i, c in enumerate(s):
            if count[ord(c) - ord('a')] == 1:
                return i
        return -1