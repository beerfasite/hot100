class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>>ans;

        sort(intervals.begin(),intervals.end());
        int st = intervals[0][0];
        int ed = intervals[0][1];
        int n = intervals.size();

        for(int i = 1;i < n;i++)
        {
            int nxt_st = intervals[i][0];
            int nxt_ed = intervals[i][1];

            if(nxt_st <= ed)
            {
                //有重叠
                ed = max(ed,nxt_ed);
            }
            else
            {
                //没有重叠
                ans.push_back({st,ed});
                st = nxt_st;
                ed = nxt_ed;
            }
        }

        ans.push_back({st,ed});

        return ans;

    }
};