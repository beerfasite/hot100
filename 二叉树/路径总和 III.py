# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,root,targetSum):
        if root is None:
            return 0

        ans = 0
        if root.val == targetSum:
            ans += 1
        ans += self.func(root.left,targetSum - root.val)
        ans += self.func(root.right,targetSum - root.val)

        return ans


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if root is None:
            return 0

        ans = self.func(root,targetSum)
        ans += self.pathSum(root.left,targetSum)
        ans += self.pathSum(root.right,targetSum)

        return ans