class Solution:
    
    def dfs(self,nums,res,path,vis):
        if len(path) == len(nums):
            res.append(path[:])
        
        for i in range(len(nums)):
            if vis[i] == True:
                continue
            
            vis[i] = True
            path.append(nums[i])
            self.dfs(nums,res,path,vis)
            vis[i] = False
            path.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        self.dfs(nums,res,path,[False] * len(nums))

        return res



"""
能取到前面的,但是不能取重复的,用vis
"""