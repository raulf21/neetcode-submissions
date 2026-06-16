class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(s, openCount, closedCount):
            if len(s) == 2*n:
                result.append(s)
                return 
            
            if openCount < n:
                backtrack(s + '(',openCount+1,closedCount)
            if closedCount < openCount:
                backtrack(s + ')',openCount,closedCount+1)

        result = []
        backtrack("",0,0)
        return result