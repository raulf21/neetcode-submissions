class Solution:
    def minOperations(self, s: str) -> int:
        cost_pattern_a = 0 # Cost to make s match "010101.."

        for i, char in enumerate(s):
            expected = str(i % 2)
            if char != expected:
                cost_pattern_a +=1

        cost_pattern_b = len(s) - cost_pattern_a

        return min(cost_pattern_a, cost_pattern_b)
        