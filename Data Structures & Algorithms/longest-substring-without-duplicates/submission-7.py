class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        L = 0
        length = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[L])
                L +=1
            charset.add(s[r])
            length = max(length, r-L + 1)
        return length
        