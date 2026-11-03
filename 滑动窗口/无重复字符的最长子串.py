class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        ans = 0
        cnt = {}

        for i in range(len(s)):
            c = s[i]
            cnt[c] = cnt.get(c,0) + 1

            while cnt[c] > 1:
                #说明有重复的了，并且是左边导致的
                cnt[s[left]] -= 1
                left += 1
            
            ans = max(ans,i - left + 1)

        return ans
