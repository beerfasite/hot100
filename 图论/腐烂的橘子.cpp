class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ans = 0;

        queue<pair<int,int>>q;
        int fresh = 0;

        int n = grid.size();
        int m = grid[0].size();
        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < m;j++)
            {
                if(grid[i][j] == 1)
                {
                    fresh++;
                }
                else if(grid[i][j] == 2)
                {
                    q.push({i,j});
                }
            }
        }

        vector<pair<int,int>>dir = {{-1,0},{1,0},{0,-1},{0,1}};
        while(!q.empty())
        {
            int k = q.size();//当前这一分钟要烂掉的橘子
            bool rotten = false;
            for(int kk = 0;kk < k;kk++)
            {
                auto x = q.front();
                q.pop();
                for(auto cur:dir)
                {
                    int i = x.first + cur.first;
                    int j = x.second + cur.second;
                    if(i >= 0 && j >= 0 && i < n && j < m && grid[i][j] == 1)
                    {
                        grid[i][j] = 2;
                        fresh--;
                        q.push({i,j});
                        rotten = true;
                    }
                }
            }
            if(rotten)ans++;
        }

        if(fresh > 0)return -1;
        else return ans;
    }
};