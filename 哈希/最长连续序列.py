class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        s = set(nums)

        for num in nums:
            if num - 1 in s:
                continue

            tmp = 1
            cur = num
            while cur + 1 in s:
                cur += 1
                tmp += 1
            
            ans = max(ans,tmp)
            if ans * 2 > len(s):
                break
        return ans