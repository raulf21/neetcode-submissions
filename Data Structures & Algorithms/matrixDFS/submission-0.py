class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c):
            # Base case: out of bounds, rock, or already visited
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                grid[r][c] == 1 or visited[r][c]):
                return 0
            
            # Base case: reached destination
            if r == rows - 1 and c == cols - 1:
                return 1
            
            # Mark current cell as visited
            visited[r][c] = True
            
            # Explore all 4 directions and sum the paths
            count = 0
            count += dfs(r + 1, c)  # down
            count += dfs(r - 1, c)  # up
            count += dfs(r, c + 1)  # right
            count += dfs(r, c - 1)  # left
            
            # Backtrack: unmark cell for other paths
            visited[r][c] = False
            
            return count
        
        return dfs(0, 0)