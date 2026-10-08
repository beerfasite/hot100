class Solution:

    def func(self,nums,st,path,res):
        res.append(path[:])
        for i in range(st,len(nums)):
            path.append(nums[i])
            self.func(nums,i + 1,path,res)
            path.pop()
    def subsets(self, nums: list[int]) -> list[list[int]]:
        path = []
        res = []
        self.func(nums,0,path,res)
        return res

        