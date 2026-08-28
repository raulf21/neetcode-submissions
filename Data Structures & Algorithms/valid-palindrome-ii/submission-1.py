class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrom_range(l: int, r: int) -> bool:
            while l<r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True
        L = 0
        R = len(s) -1 

        while L<R:
            if s[L] != s[R]:
                # skip either L or R
                return is_palindrom_range(L+1, R) or is_palindrom_range(L, R-1)
            L +=1
            R-=1
        return True
        