class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        
        for i in range(len(shortest_word)):
            char = shortest_word[i]
            for word in strs:
                if word[i] != char:  # mismatch found
                    return shortest_word[:i]  # return prefix up to i
        return shortest_word  # all chars matched