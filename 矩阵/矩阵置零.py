class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])

        row_0 = [False] * n
        col_0 = [False] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_0[i] = True
                    col_0[j] = True
        
        for i in range(n):
            for j in range(m):
                if row_0[i] or col_0[j]:
                    matrix[i][j] = 0

        