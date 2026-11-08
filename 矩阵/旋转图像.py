class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])

        vis = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if vis[i][j] == False and vis[j][i] == False:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                    vis[i][j] = True
                    vis[j][i] = True

        def reverse(i,j,nums):
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1


        for i in range(n):
            #遍历每一行
            row = matrix[i]
            reverse(0,m - 1,row)
        
