class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int>ans(n - k + 1);
        deque<int>q;

        for(int i = 0;i < nums.size();i++)
        {
            //右边进入
            while(!q.empty() && nums[q.back()] <= nums[i])
            {
                q.pop_back();
            }
            q.push_back(i);

            //左边出去,l是队列的左边界
            int l = i - k + 1;
            if(q.front() < l)q.pop_front();

            if(l >= 0)
            {
                ans[l] = nums[q.front()];
            }
            
        }
        return ans;
    }
};