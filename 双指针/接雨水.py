class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(height[i],left_max[i - 1])
        
        right_max[-1] = height[-1]
        for i in range(n - 2,-1,-1):
            right_max[i] = max(right_max[i + 1],height[i])

        ans = 0
        for l,r,h in zip(left_max,right_max,height):
            ans += min(l,r) - h
        
        return ans