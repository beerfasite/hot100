# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        self.ans = 0
        self.depth = 0
        self.dfs(root)
        return self.ans

    def dfs(self,root):
        if root is None:
            return 
        self.depth += 1
        self.ans = max(self.ans, self.depth)

        self.dfs(root.left)
        self.dfs(root.right)

        self.depth -= 1
