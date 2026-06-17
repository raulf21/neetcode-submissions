class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for p in parts:
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.' or p=="":
                continue
            else:
                stack.append(p)
        result = '/' + '/'.join(stack)
        return result
        