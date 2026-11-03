class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        s = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s[i + 1] = s[i] + nums[i]

        cnt = {}
        ans = 0
        #s[j] - s[i] = k,s[i] = s[j] - k
        for sj in s:
            if sj - k in cnt:
                ans += cnt[sj - k]
            cnt[sj] = cnt.get(sj,0) + 1
        
        return ans