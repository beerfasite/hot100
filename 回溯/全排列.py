class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        vis = [False] * len(nums)

        self.func(nums,res,path,vis)

        return res

    def func(self,nums,res,path,vis):
        if len(path) == len(nums):
            res.append(path[:])
        
        for i in range(len(nums)):
            if vis[i] == True:
                continue
            path.append(nums[i])
            vis[i] = True
            self.func(nums,res,path,vis)
            path.pop()
            vis[i] = False
        