class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans,hp = 0,0
        for x in nums:
            if hp == 0:
                hp += 1
                ans = x
            else:
                if x == ans:
                    hp += 1
                else:
                    hp -= 1
        return ans
