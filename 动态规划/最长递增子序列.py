class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        
        dp = [1] * length
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        res = 0
        for v in dp:
            res = max(res, v)
        return res