class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        L = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[L])
                L +=1
            charset.add(s[r])
            res = max(res, r - L + 1)
        return res
