class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        //dp[i]表示当前i下标的最大和
        int n = nums.size();
        vector<int>dp(n);

        dp[0] = nums[0];
        int ans = nums[0];

        for(int i = 1;i < n;i++)
        {
            int s = dp[i - 1] + nums[i];//选当前的话
            dp[i] = max(nums[i],s);
            ans = max(ans,dp[i]);
        }

        return ans;


    }
};