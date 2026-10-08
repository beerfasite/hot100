class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size(); // 轮转 k 次等同于轮转 k % n 次
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};

