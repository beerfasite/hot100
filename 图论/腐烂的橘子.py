class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = []
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        ans = 0
        while q and fresh:
            ans += 1
            tmp = q
            q = []
            for x,y in tmp:
                for i,j in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    if 0<=i<n and 0<=j<m and grid[i][j] == 1:
                        q.append((i,j))
                        grid[i][j] = 2
                        fresh -= 1
            
        return -1 if fresh else ans