class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        ans = []

        for i in range(0,len(nums) - 2):
            #有重复数字
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #提前结束
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            #当前这一轮太小
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue


            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans