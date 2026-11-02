class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        循环不变量：在循环过程中，nums 的数据分布始终如下图
        [ 非零元素 | 零元素 | 尚未遍历 ]
                    ^       ^
                    start0  i
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[idx] = nums[idx],nums[i]
                idx += 1
        return nums