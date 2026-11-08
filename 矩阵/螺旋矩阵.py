class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        ans = []
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

        n = len(matrix)
        m = len(matrix[0])

        vis = [[False] * m for _ in range(n)]

        x = 0
        y = 0
        k = 0

        for i in range(n * m):
            ans.append(matrix[x][y])
            vis[x][y] = True

            nxt_x = x + dx[k]
            nxt_y = y + dy[k]
            if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y >= m or vis[nxt_x][nxt_y] == True:
                k = (k + 1) % 4
                nxt_x = x + dx[k]
                nxt_y = y + dy[k]

            x = nxt_x
            y = nxt_y
            
        return ans