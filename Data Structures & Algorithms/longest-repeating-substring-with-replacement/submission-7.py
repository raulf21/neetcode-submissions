class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        length = 0
        L = 0
        maxf = 0
        for R in range(len(s)):
            hashMap[s[R]] = 1 + hashMap.get(s[R], 0)
            maxf = max(maxf, hashMap[s[R]])

            while (R - L +1) - maxf > k:
                hashMap[s[L]] -=1
                L +=1

            length = max(length, R-L + 1)
        return length

        