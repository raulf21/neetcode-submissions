class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')':'(',']':'[',"}":"{"}

        for char in s:
            if char not in valid:
                stack.append(char)
            else:
                if not stack or stack[-1] != valid[char]:
                    return False
                else:
                    stack.pop()
        return not stack        