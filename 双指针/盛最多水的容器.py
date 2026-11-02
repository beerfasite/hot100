class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            s = (right - left) * min(height[left],height[right])
            ans = max(s,ans)

            if height[left] < height[right]:
                #left更加矮
                left += 1
            else:
                right -= 1
        return ans