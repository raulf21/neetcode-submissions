class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Gravity
        for row in range(m):
            empty_slot = n - 1
            for col in range(n-1, -1, -1):
                if boxGrid[row][col] == '*':
                    empty_slot = col - 1
                if boxGrid[row][col] == '#':
                    boxGrid[row][col], boxGrid[row][empty_slot] = boxGrid[row][empty_slot], boxGrid[row][col]
                    empty_slot -= 1
        result = [['.'] * m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                result[col][m-1 - row] = boxGrid[row][col]
        return result 

        
        
