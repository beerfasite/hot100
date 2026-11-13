# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,root):
        if root is  None:
            return
        self.func(root.left)
        self.res.append(root.val)
        self.func(root.right)

    def isValidBST(self, root: TreeNode | None) -> bool:
        self.res = []
        self.func(root)

        for i in range(1,len(self.res)):
            if self.res[i - 1] >= self.res[i]:
                return False

        return True
