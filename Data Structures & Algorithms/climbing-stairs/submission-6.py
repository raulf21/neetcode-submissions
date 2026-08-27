class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(step: int) -> int:
            if step <= 2:
                return step

            # If already computed, return cached answer
            if step in cache:
                return cache[step]

            cache[step] = helper(step-1) + helper(step-2)
            return cache[step]
        return helper(n)


        