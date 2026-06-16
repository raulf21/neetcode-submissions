class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        queue = deque([(0,0,0)]) # rows, cols, distance
        visited[0][0] = True

        while queue:
            r, c, distance = queue.popleft()

            if r == rows - 1 and c == cols -1:
                return distance
            
            for dr, dc in [[1,0], [-1,0], [0,1], [0, -1]]:
                nr, nc = r + dr, c + dc

                if (0<=nr<rows and 0<= nc < cols and
                    grid[nr][nc] == 0 and not visited[nr][nc]):
                    visited[nr][nc] = True
                    queue.append((nr, nc, distance + 1))

        return -1

        