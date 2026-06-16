class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(i, combo, k):
            if len(combo) == k:
                res.append(combo.copy())
                return 
            needed = k - len(combo)

            for j in range(i, n-needed+2):
                combo.append(j)
                backtrack(j+1, combo, k)
                combo.pop()

            
        backtrack(1, [],k)

        return res
        