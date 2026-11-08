class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pre = [1] * (n + 1)
        back = [1] * (n + 1)

        for i in range(1,n):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(n - 2,-1,-1):
            back[i] = back[i + 1] * nums[i + 1]

        ans = []
        for i in range(n):
            ans.append(pre[i] * back[i])

        return ans