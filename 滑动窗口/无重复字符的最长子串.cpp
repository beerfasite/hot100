class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        int left = 0;

        unordered_map<char,int>cnt;

        for(int i = 0;i < s.size();i++)
        {
            //i是右边界
            char c = s[i];
            cnt[c]++;

            while(cnt[c] > 1)
            {
                //说明不符合要求了,并且是由于左边的原因
                cnt[s[left]]--;
                left++;
            }

            ans = max(ans,i - left + 1);
        }

        return ans;
    }
};