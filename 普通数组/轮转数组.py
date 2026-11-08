class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,j):
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
                i += 1
        
        k = k % len(nums)
        reverse(0,len(nums) - 1)
        reverse(0,k - 1)
        reverse(k,len(nums) - 1)
