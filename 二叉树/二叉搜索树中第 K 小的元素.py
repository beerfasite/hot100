# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,root):
        if root is None:
            return 
        self.func(root.left)
        self.res.append(root.val)
        self.func(root.right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.func(root)

        return self.res[k - 1]

