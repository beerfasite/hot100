class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        x = n - 1
        y = 0

        while x >= 0 and y < m:
            v = matrix[x][y]
            if v > target:
                x -= 1
            elif v < target:
                y += 1
            else:
                return True
        return False