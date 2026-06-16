class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            self.prefix[r][0] = matrix[r][0]
            for c in range(1, cols):
                self.prefix[r][c] = self.prefix[r][c-1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prefix[row][col2] - self.prefix[row][col1-1]
            else:
                res += self.prefix[row][col2]

        return res