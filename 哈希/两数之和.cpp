

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>res;
        unordered_map<int,int>mp;
        
        for(int i = 0;i < nums.size();i++)
        {
            int e = nums[i];
            if(mp.count(target - e))
            {
                //找到了
                res.push_back(i);
                res.push_back(mp[target - e]);
            }
            else
            {
                mp[e] = i;
            }
        }
        return res;
    }
};

