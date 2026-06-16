class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        res = []

        if not digits:
            return []
        def backtrack(i, subset):
            if i == len(digits):
                res.append(subset)
                return 
            for letter in phone[digits[i]]:
                # no need to pop() because strings are immutable 
                # new string is created for next call

                backtrack(i + 1, subset + letter)
            
        backtrack(0, "")
        return res        