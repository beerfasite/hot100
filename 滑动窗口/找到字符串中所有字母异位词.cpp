class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char,int>p_cnt;
        for(int i = 0;i < p.size();i++)p_cnt[p[i]]++;

        vector<int>ans;

        unordered_map<char,int>s_cnt;

        int l = 0;
        for(int i = 0;i < s.size();i++)
        {
            //检查窗口合理
            int w = i - l + 1;
            if(w > p.size())
            {
                s_cnt[s[l]]--;
                if(s_cnt[s[l]] == 0)
                {
                    //为0了，得直接删除
                    s_cnt.erase(s[l]);
                }
                l++;
            }
            
            s_cnt[s[i]]++;//当前遇到的

            if(s_cnt == p_cnt)
            {
                ans.push_back(l);
            }

        }
        return ans;
    }
};