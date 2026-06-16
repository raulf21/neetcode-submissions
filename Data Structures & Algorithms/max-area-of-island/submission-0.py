class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0, 1), (-1,0), (0,-1)]
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c]==0 or (r,c) in visit):
                return 0

            visit.add((r,c))
            res = 1
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   area = max(area, dfs(r, c))
        return area