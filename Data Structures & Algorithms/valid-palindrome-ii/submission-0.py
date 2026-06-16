class Solution:
    def validPalindrome(self, s: str) -> bool:
        


        def is_palindrom(l,r):
            while l< r:
                if s[l] != s[r]:
                    return False
                l +=1 
                r -=1
            return True
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                # Try deleting left character(l+1, r) OR right character(l, r+1)
                return is_palindrom(l+1, r) or is_palindrom(l, r- 1)
            l +=1
            r -=1
        return True # no mismatch found -> already a palindrome