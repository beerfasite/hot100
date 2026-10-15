class Solution:
    def lower_bound(self,nums,target):
        left = 0
        right = len(nums) -1 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.lower_bound(nums,target)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        right = self.lower_bound(nums,target + 1) - 1
        return [left,right]