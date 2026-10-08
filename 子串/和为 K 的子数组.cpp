class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> s(n + 1);

        for (int i = 0; i < n; i++) 
        {
            s[i + 1] = s[i] + nums[i];
        }

        unordered_map<int, int> cnt;
        int ans = 0;
        for (int sj : s) 
        {
            int target = sj - k;
            if (cnt.count(target) > 0) 
            {
                ans += cnt[target];
            } 

            cnt[sj]++;
        }
        return ans;
    }
};
