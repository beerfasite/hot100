class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        p_cnt = {}
        for c in p:
            p_cnt[c] = p_cnt.get(c,0) + 1

        ans = []
        s_cnt = {}
        l = 0

        for i in range(len(s)):
            w = i - l + 1
            if w > len(p):
                s_cnt[s[l]] -= 1
                if s_cnt[s[l]] == 0:
                    del s_cnt[s[l]]
                l += 1
            s_cnt[s[i]] = s_cnt.get(s[i],0) + 1
            if s_cnt == p_cnt:
                ans.append(l)
        
        return ans