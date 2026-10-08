class Solution:
    def climbStairs(self, n: int) -> int:
        dp0 = 1
        dp1 = 1
        for _ in range(2,n+1):
            dp2 = dp1 + dp0
            dp0 = dp1
            dp1 = dp2
        return dp1