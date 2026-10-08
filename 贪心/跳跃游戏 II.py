class Solution:
    def jump(self, nums: list[int]) -> int:
        step = 0
        maxr = 0#一次性跳的最远距离到哪里
        maxstep = 0#一次性跳的最远距离

        if len(nums) == 1:
            return 0
        
        for i in range(len(nums) - 1):
            if i <= maxstep:
                maxstep = max(maxstep,nums[i] + i)
                if i == maxr:
                    step += 1
                    maxr = maxstep

        return step