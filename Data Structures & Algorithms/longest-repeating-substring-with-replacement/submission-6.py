class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxFrequency = 0
        L = 0
        max_length = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxFrequency = max(maxFrequency, hashmap[s[r]])

            while (r - L + 1) - maxFrequency > k:
                hashmap[s[L]] -=1
                L +=1
            max_length = max(max_length, r - L + 1)
        return max_length

