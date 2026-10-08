class Solution {
    void dfs(vector<vector<char>>& grid,int x,int y)
    {
        int n = grid.size();
        int m = grid[0].size();
        if(x < 0 || y < 0 || x > n - 1 || y > m - 1 || grid[x][y] == '2' || grid[x][y] == '0')return;

        grid[x][y] = '2';

        dfs(grid,x + 1,y);
        dfs(grid,x - 1,y);
        dfs(grid,x,y + 1);
        dfs(grid,x,y - 1);

    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int ans = 0;

        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < m;j++)
            {
                if(grid[i][j] == '1')
                {
                    dfs(grid,i,j);
                    ans++;
                }
            }
        }

        return ans;
    }
};