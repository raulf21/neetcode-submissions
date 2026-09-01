class Solution:

    def expand_around_center(self,s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1
            return s[l+1: r]
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            # Expand assuming an ODD length cetner
            odd_palindrome = self.expand_around_center(s,i,i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            # expand assuming an even length cetner
            even_palindrome = self.expand_around_center(s, i, i+1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        return longest


        