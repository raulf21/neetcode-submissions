class Solution:
    def firstUniqChar(self, s: str) -> int:
        count ={}
        # count frequencies of each char
        for char in s:
            count[char] = 1 + count.get(char, 0)

        # Find first character with a count of 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        
        return -1