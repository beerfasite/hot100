class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        #key是num，value是下标
        for idx,value in enumerate(nums):
            if target - value in hash_map:
                return[hash_map[target - value],idx]
            hash_map[value] = idx
        return []