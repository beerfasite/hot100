class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;

        unordered_set<int>s(nums.begin(),nums.end());

        for(int i = 0;i < nums.size();i++)
        {
            int e = nums[i];

            //先检查e-1在不在
            if(s.count(e - 1) > 0)continue;


            //不在e - 1，那么e就是当前序列的第一个元素
            int tmp = 1;
            while(s.count(++e) > 0)
            {
                tmp++;
            }

            ans = max(ans,tmp);
            if(ans * 2 > nums.size())return ans;
        }
        return ans;
    }
};