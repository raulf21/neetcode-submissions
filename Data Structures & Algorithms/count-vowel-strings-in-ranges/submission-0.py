class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        P = [0] * ( n + 1)

        for i in range(n):
            word = words[i]
            # Check if word starts and ends with vowel
            if word[0] in vowels and word[-1] in vowels:
                is_valid = 1
            else: 
                is_valid = 0

            P[i+1] = P[i] + is_valid
        ans = []
        for a, b in queries:
            ans.append(P[b+1] - P[a])
        return ans

        