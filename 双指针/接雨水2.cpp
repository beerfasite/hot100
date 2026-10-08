class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int left = 0;
        int right = height.size() - 1;

        int s1 = 0;
        int s2 = 0;

        while(left <= right)
        {
            s1 = max(s1,height[left]);
            s2 = max(s2,height[right]);

            if(s1 < s2)
            {
                //前面的板子接的水确定了
                ans += s1 - height[left];
                left++;
            }
            else
            {
                ans += s2 - height[right];
                right--;
            }
        }

        return ans;
    }
};