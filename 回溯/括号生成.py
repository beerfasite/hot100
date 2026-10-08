class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = [''] * (2 * n)

        def dfs(left,right):
            if right == n:
                res.append(''.join(path))
                return
            
            if left < n:
                path[left + right] = '('
                dfs(left + 1,right)
            
            if right < left:
                path[left + right] = ')'
                dfs(left,right + 1)
        dfs(0,0)
        return res