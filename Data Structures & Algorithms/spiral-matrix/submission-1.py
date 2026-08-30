class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        result = []
        while left <= right and top <=bottom:
            # traverse right (across the top row)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top +=1 
            # if left has reached right, update top +=1
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -=1
            # traverse left across the bottom row
            # must check if top <= bottom because we incremented top above 
            if top <= bottom:
                for col in range(right, left-1,-1):
                    result.append(matrix[bottom][col])
                bottom -=1

            # traverse up along left column
            # must check if left <=right because we decremented right above
            if left<=right:
                for row in range(bottom, top -1, -1):
                    result.append(matrix[row][left])
                left +=1

        return result
            
        