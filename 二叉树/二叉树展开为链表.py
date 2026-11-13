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
        self.res.append(root)
        self.func(root.left)
        self.func(root.right)


    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []
        self.func(root)

        for i in range(1,len(self.res)):
            left = self.res[i - 1]
            right = self.res[i]
            left.left = None
            left.right = right
