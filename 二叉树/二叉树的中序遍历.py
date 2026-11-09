# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,ans):
        if root is None:
            return 
        self.dfs(root.left,ans)
        ans.append(root.val)
        self.dfs(root.right,ans)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        self.dfs(root,ans)

        return ans