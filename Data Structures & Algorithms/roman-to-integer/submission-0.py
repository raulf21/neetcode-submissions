class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        n = len(s)
        total = 0
        for i in range(n):
            # Check if there's a next character and it's larger
            if i + 1 < n and symbols[s[i]] < symbols[s[i+1]]:
                total -= symbols[s[i]] # subtract current
            else:
                total += symbols[s[i]]
        return total
