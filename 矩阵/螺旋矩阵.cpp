class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>ans;

        if(matrix[0].size() == 0)return ans;

        //右下左上
        int dx[4] = {0,1,0,-1};
        int dy[4] = {1,0,-1,0};

        int n = matrix.size();//行
        int m = matrix[0].size();//列
        
        int x = 0;
        int y = 0;
        int k = 0;
        vector<vector<bool>>vis(n,vector<bool>(m,false));//访问数组

        for(int i = 1;i <= n * m;i++)
        {
            ans.push_back(matrix[x][y]);
            vis[x][y] = true;
            int xx = x + dx[k];
            int yy = y + dy[k];
            if(xx < 0 || xx >= n ||yy < 0 || yy >= m || vis[xx][yy] == true)
            {
                k = (k + 1) % 4;
                xx = x + dx[k];
                yy = y + dy[k];
            }

            x = xx;
            y = yy;
        }

        return ans;
    }
};