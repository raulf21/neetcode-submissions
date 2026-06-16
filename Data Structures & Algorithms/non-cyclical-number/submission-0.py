class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumSquareDigits(n):
            total = 0
            while n > 0:
                digit = n % 10 
                total += digit * digit
                n = n // 10
            return total

        slow, fast = n, sumSquareDigits(n)

        while fast != 1 and slow != fast:
            slow = sumSquareDigits(slow)
            fast = sumSquareDigits(sumSquareDigits(fast))
        return fast == 1
