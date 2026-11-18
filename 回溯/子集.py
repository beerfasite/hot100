class Solution:

    def dfs(self,nums,st,res,path):

        res.append(path[:])
        for i in range(st,len(nums)):
            path.append(nums[i])
            self.dfs(nums,i + 1,res,path)
            path.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        self.dfs(nums,0,res,path)

        return res


"""
不能取到前面的，间接保证了不能取到重复的了
"""