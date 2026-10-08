class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxl = 0
        for i in range(len(nums)):
            if i <= maxl:
                #在最远范围内
                maxl = max(maxl,nums[i] + i)
                if maxl >= len(nums) - 1:
                    return True
            else:
                return False

